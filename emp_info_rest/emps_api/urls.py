from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello_api),
    path('data/',views.get_data),
    path('get_single/<id>',views.get_single)
    
]
