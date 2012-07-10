import json
from xml.etree import ElementTree

from celery.task import task
from django.conf import settings
import requests

from antitrust.models import EveItem, EveNearestStation, REGION_FORGE
from antitrust.utils import update

@task(ignore_result=True)
def update_prices():
    qs = EveItem.objects.all()
    params = {'regionlimit': REGION_FORGE, 'typeid': []}
    for item in qs:
        params['typeid'].append(item.eve_id)
    response = requests.get('http://api.eve-central.com/api/marketstat', params=params)
    response.raise_for_status()
    tree = ElementTree.fromstring(response.text)
    prices = {}
    for item in tree.findall('.//type'):
        prices[int(item.attrib['id'])] = {
            'mean_sell': item.find('./sell/avg').text,
            'mean_buy': item.find('./buy/avg').text,
            'mean_all': item.find('./all/avg').text,
            'median_sell': item.find('./sell/median').text,
            'median_buy': item.find('./buy/median').text,
            'median_all': item.find('./all/median').text,
            'min_sell': item.find('./sell/min').text,
            'max_buy': item.find('./buy/max').text,
        }
    for item in qs:
        update(item.forge_prices, **prices[item.eve_id])

@task(ignore_result=True)
def update_assets():
    params = {'keyID': settings.EVE_API_KEY_ID, 'vCode': settings.EVE_API_VCODE}
    response = requests.get('https://api.eveonline.com/corp/AssetList.xml.aspx', params=params)
    response.raise_for_status()
    tree = ElementTree.fromstring(response.text)
    assets = {}
    for row in tree.findall('.//row'):
        typeid = int(row.attrib['typeID'])
        assets[typeid] = assets.get(typeid, 0) + int(row.attrib['quantity'])
    for item in EveItem.objects.all():
        update(item, corp_count=assets.get(item.eve_id, 0))

@task(ignore_result=True)
def find_nearest_station(system_id):
    routes = []
    for target in EveNearestStation.ALLOWED_SYSTEMS.iterkeys():
        response = requests.get('http://api.eve-central.com/api/route/from/%s/to/%s'%(system_id, target))
        response.raise_for_status()
        route_data = json.loads(response.text)
        routes.append((len(route_data), target))
    routes.sort(key=lambda x: x[0])
    data = {
        'system_id': system_id,
        'creation_hash': EveNearestStation.objects.current_hash(),
        'nearest_system': str(routes[0][1]),
        'nearest_station': str(EveNearestStation.ALLOWED_SYSTEMS.get(routes[0][1], 0)),
    }
    EveNearestStation.objects.create(**data)
