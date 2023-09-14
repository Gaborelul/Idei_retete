# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from micdejun.forms import MicdejunForm
from micdejun.models import Micdejun


class MicdejunCreateView(CreateView):
    template_name = 'micdejun/create_micdejun.html'
    model = Micdejun
    form_class = MicdejunForm
    success_url = reverse_lazy('list-of-micdejun')


class MicdejunListView(ListView):
    template_name = 'micdejun/list_of_micdejun.html'
    model = Micdejun
    context_object_name = 'all_micdejuns'


def search(request):
    get_value = request.Get.get('filter')
    if get_value:
        micdejun = Micdejun.objects.filter(name__icontains=get_value)
    else:
        micdejun = Micdejun.objects.all()
    return render(request, 'micdejun/list_of_micdejun.html', {'all_micdejuns': micdejun})
