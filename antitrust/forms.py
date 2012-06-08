from django import forms
from django.utils.translation import ugettext as _

from bootstrap.forms import BootstrapForm

class ItemValidator(object):
    def __init__(self, item):
        self.item = item

    def __call__(self, value):
        if value + self.item.corp_count > self.item.corp_optimal:
            raise forms.ValidationError(_('We do not need that many'))

class PIPurchaseForm(BootstrapForm):
    class Meta:
        help_style = 'inline'

    def __init__(self, *args, **kwargs):
        self.__items = kwargs.pop('items', [])
        self.__max_price = kwargs.pop('max_price', None)
        super(PIPurchaseForm, self).__init__(*args, **kwargs)
        for item in self.__items:
            if item.demand:
                field_args = {
                    'label': item.name,
                    'min_value': 0,
                    'help_text': 'Price %s ISK'%item.price,
                    'initial': 0,
                    'validators': [ItemValidator(item)],
                }
                self.fields['item_%s'%item.eve_id] = forms.IntegerField(**field_args)

    def clean(self):
        cleaned_data = super(PIPurchaseForm, self).clean()
        cleaned_data['total'] = 0
        for item in self.__items:
            cleaned_data['total'] += cleaned_data.get('item_%s'%item.eve_id, 0) * item.price
        if self.__max_price and cleaned_data['total'] > self.__max_price:
            raise forms.ValidationError(_('We do not need that many'))
        if cleaned_data['total'] == 0:
            raise forms.ValidationError(_('You need to sell us something'))
        return cleaned_data
