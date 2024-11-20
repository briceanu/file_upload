from django.urls import include,path
from . import views

 


urlpatterns = [
    path('create_list',views.CreateListAPI.as_view(),name='list_create'),

    ]