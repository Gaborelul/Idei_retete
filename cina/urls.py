from django.urls import path

from cina import views

urlpatterns = [
    path('create_cina/', views.CinaCreateView.as_view(), name='create-cina'),
    path('list_of_cina/', views.CinaListView.as_view(), name='list-of-cina'),

]
