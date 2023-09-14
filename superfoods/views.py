from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from superfoods.forms import SuperfoodsForm
from superfoods.models import Superfoods


# Create your views here.


class SuperfoodsCreateView(CreateView):
    template_name = 'superfoods/create_superfoods.html'
    model = Superfoods
    form_class = SuperfoodsForm
    success_url = reverse_lazy('list-of-superfoods')


class SuperfoodsListView(ListView):
    template_name = 'superfoods/list_of_superfoods.html'
    model = Superfoods
    context_object_name = 'all_superfoods'
