from xml.etree import ElementTree

from celery.task import task
from django.conf import settings
import requests

from antitrust.models import EveItem
from antitrust.utils import update

# Just hard-code this for the moment
REGION_FORGE = 10000002

@task
def update_prices(group_id):
    qs = EveItem.objects.filter(eve_group_id=group_id)
    params = {'regionlimit': REGION_FORGE, 'typeid': []}
    for item in qs:
        params['typeid'].append(item.eve_id)
    response = requests.get('http://api.eve-central.com/api/marketstat', params=params)
    response.raise_for_status()
    tree = ElementTree.fromstring(response.text)
    prices = {}
    for item in tree.findall('.//type'):
        prices[int(item.attrib['id'])] = item.find('./all/avg').text
    for item in qs:
        update(item, forge_price=prices[item.eve_id])

@task
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
