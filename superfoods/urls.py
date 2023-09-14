from django.urls import path

from superfoods import views

urlpatterns = [
    path('create_superfoods/', views.SuperfoodsCreateView.as_view(), name='create-superfoods'),
    path('list_of_superfoods/', views.SuperfoodsListView.as_view(), name='list-of-superfoods'),

]
