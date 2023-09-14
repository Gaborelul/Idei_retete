from django.urls import path

from micdejun import views

urlpatterns = [
    path('create_micdejun/', views.MicdejunCreateView.as_view(), name='create-micdejun'),
    path('list_of_micdejun/', views.MicdejunListView.as_view(), name='list-of-micdejun'),
    path('search/', views.search, name='search'),
]
