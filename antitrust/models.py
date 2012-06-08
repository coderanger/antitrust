from django.db import models
from django.utils.translation import ugettext_lazy as _

class EveItem(models.Model):
    name = models.CharField(_('Name'), max_length=255, unique=True)
    eve_id = models.IntegerField(_('EVE ID'), unique=True)
    eve_group_id = models.IntegerField(_('EVE Group ID'), default=0)
    forge_price = models.DecimalField(_('Forge Price'), max_digits=7, decimal_places=2, default=0)
    corp_count = models.IntegerField(_('Corporation Count'), default=0)
    corp_optimal = models.IntegerField(_('Corporation Optimal Count'), default=0)

    @property
    def price(self):
        return self.forge_price

    @property
    def demand(self):
        if self.corp_count >= self.corp_optimal:
            return False
        return True