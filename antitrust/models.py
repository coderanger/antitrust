from decimal import Decimal

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Just hard-code this for the moment
REGION_FORGE = 10000002

class EveItem(models.Model):
    name = models.CharField(_('Name'), max_length=255, unique=True)
    eve_id = models.IntegerField(_('EVE ID'), unique=True)
    eve_group_id = models.IntegerField(_('EVE Group ID'), default=0)
    corp_count = models.IntegerField(_('Corporation Count'), default=0)
    corp_optimal = models.IntegerField(_('Corporation Optimal Count'), default=0)

    @property
    def price(self):
        if self.corp_optimal == 0:
            return self.forge_prices.median_sell
        return (((((self.forge_prices.median_sell-Decimal('10'))))/Decimal('100'))*(Decimal('87.5')-(((self.corp_count/self.corp_optimal)-Decimal('0.5'))*Decimal('10')))) - (self.forge_prices.median_sell*((self.corp_count/self.corp_optimal)*Decimal('0.2')))

    @property
    def demand(self):
        if self.corp_count >= self.corp_optimal:
            return False
        if self.price <= 0:
            return False
        return True

    @property
    def forge_prices(self):
        if not hasattr(self, '_forge_prices'):
            self._forge_prices, created = self.prices.get_or_create(region=REGION_FORGE)
        return self._forge_prices

class EveItemPrices(models.Model):
    item = models.ForeignKey(EveItem, related_name='prices')
    region = models.IntegerField(_('Region'))
    mean_sell = models.DecimalField(_('Mean Sell Price'), max_digits=7, decimal_places=2, default=0)
    mean_buy = models.DecimalField(_('Mean Buy Price'), max_digits=7, decimal_places=2, default=0)
    mean_all = models.DecimalField(_('Mean Price'), max_digits=7, decimal_places=2, default=0)
    median_sell = models.DecimalField(_('Median Sell Price'), max_digits=7, decimal_places=2, default=0)
    median_buy = models.DecimalField(_('Median Buy Price'), max_digits=7, decimal_places=2, default=0)
    median_all = models.DecimalField(_('Median Price'), max_digits=7, decimal_places=2, default=0)
