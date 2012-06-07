import json
import os

from django.core.management.base import BaseCommand
from django.conf import settings

from antitrust.models import EveItem
from antitrust.utils import update

class Command(BaseCommand):
    args = '<fixture_id>'
    help = 'Loads data about EVE items from a fixture'

    def locate_fixture(self, name):
        return os.path.join(settings.PROJECT_ROOT, 'antitrust', 'fixtures', name + '.json')

    def handle(self, *args, **options):
        for fixture_name in args:
            path = self.locate_fixture(fixture_name)
            data = json.load(open(path, 'rb'))
            for eve_id, item_data in data.iteritems():
                it, created = EveItem.objects.get_or_create(eve_id=eve_id, defaults=item_data)
                if created:
                    update(it, **item_data)
