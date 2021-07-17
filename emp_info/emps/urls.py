
from django.urls import path
from .views import EmpPersonal_Delete, EmpPersonal_Details, EmpPersonal_List, EmpPersonal_Update, basic_load, delete_user, get_single_data, get_user_list, new_password, update_data, user_html_form, user_login, user_logout, user_register,user_model_form,user_form,user_html_form,get_user_list,delete_user,user_login,user_logout, user_send_email,verify_otp,new_password
from .views import HelloSample ,EmpPersonal_cls



urlpatterns = [
    path('user_register',user_register, name='user_register'),
    path('basic/',basic_load, name='basic_load'),
    path('model_form/',user_model_form,name='user_model_form'),
    path('form/',user_form,name='user_form'),
    path('html_form/',user_html_form,name='user_html_form'),
    path('',get_user_list,name='get_user_list'),
    path('get_single/<id>',get_single_data,name='get_single_data'),
    path('update_data/<id>',update_data,name='update_data'),
    path('delete_data/<id>',delete_user,name='delete_user'),
    path('login/',user_login,name='user_login'),
    path('logout/',user_logout,name='user_logout'),
    path('user_send_email/',user_send_email,name='user_send_email'),
    path('verify_otp/',verify_otp,name='verify_otp'),
    path('new_password/<id>',new_password,name='new_password'),
    path('hello_cls/',HelloSample.as_view(),name='hello_cls'),
    path('emppersonal_cls_form',EmpPersonal_cls.as_view(),name='emppersonal_cls_form'),
    path('emppersonal_cls_list',EmpPersonal_List.as_view(),name='emppersonal_cls_list'),
    path('emppersonal_cls_update/<pk>',EmpPersonal_Update.as_view(),name='emppersonal_cls_update'),
    path('emppersonal_cls_delete/<pk>',EmpPersonal_Delete.as_view(),name='emppersonal_cls_delete'),
    path('emppersonal_cls_details/<pk>',EmpPersonal_Details.as_view(),name='emppersonal_cls_details')

]