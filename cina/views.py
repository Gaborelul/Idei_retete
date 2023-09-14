from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from cina.forms import CinaForm
from cina.models import Cina


# Create your views here.


class CinaCreateView(CreateView):
    template_name = 'cina/create_cina.html'
    model = Cina
    form_class = CinaForm
    success_url = reverse_lazy('list-of-cina')


class CinaListView(ListView):
    template_name = 'cina/list_of_cina.html'
    model = Cina
    context_object_name = 'all_cina'
