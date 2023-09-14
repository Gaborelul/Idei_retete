from django.urls import path

from pranz import views

urlpatterns = [
    path('create_pranz/', views.PranzCreateView.as_view(), name='create-pranz'),
    path('list_of_pranz/', views.PranzListView.as_view(), name='list-of-pranz'),

]
