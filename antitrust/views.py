from django.template.response import TemplateResponse

from antitrust.forms import PIPurchaseForm
from antitrust.models import EveItem, EveNearestStation

def index(request):
    return TemplateResponse(request, 'index.html', {})

def pi(request):
    items = EveItem.objects.all().order_by('name')
    if request.method == 'POST':
        form = PIPurchaseForm(request.POST, items=items)
        if form.is_valid():
            item_data = []
            for item in items:
                count = form.cleaned_data.get('item_%s'%item.eve_id, 0)
                if count > 0:
                    item_data.append({'item': item, 'count': count, 'subtotal': item.price * count})
            if request.META.get('HTTP_EVE_TRUSTED', '').lower() == 'yes':
                nearest = EveNearestStation.objects.get_for_system(request.META['HTTP_EVE_SOLARSYSTEMID'])
            else:
                nearest = None
            return TemplateResponse(request, 'pi_finish.html', {'item_data': item_data, 'total': form.cleaned_data['total'], 'nearest': nearest})
    else:
        form = PIPurchaseForm(items=items)
    return TemplateResponse(request, 'pi.html', {'form': form})
