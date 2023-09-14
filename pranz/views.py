from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from pranz.forms import PranzForm
from pranz.models import Pranz


# Create your views here.


class PranzCreateView(CreateView):
    template_name = 'pranz/create_pranz.html'
    model = Pranz
    form_class = PranzForm
    success_url = reverse_lazy('list-of-pranz')


class PranzListView(ListView):
    template_name = 'pranz/list_of_pranz.html'
    model = Pranz
    context_object_name = 'all_pranz'

