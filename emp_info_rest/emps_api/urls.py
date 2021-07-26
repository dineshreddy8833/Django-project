from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.hello_api),
    path('data/',views.get_data),
    path('get_single/<id>',views.get_single),
    path('change_password/<id>', views.change_password),
    path('cls_list/',views.EmpersonalListView.as_view()),
    path('detail_view/<id>',views.EmpersonalDetailView.as_view())
    
]
