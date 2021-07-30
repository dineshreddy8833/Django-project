from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'empviewsets', views.EmpViewset, basename='user')
# urlpatterns = router.urls

urlpatterns = [
    path('hello/',views.hello_api),
    path('data/',views.get_data),
    path('get_single/<id>',views.get_single),
    path('change_password/<id>', views.change_password),
    path('cls_list/',views.EmpersonalListView.as_view()),
    path('detail_view/<id>',views.EmpersonalDetailView.as_view()),
    path('generic_list/',views.EmpList_Generic.as_view()),
    path('generic_create/',views.EmpCreate_Generic.as_view()),
    path('generic_retrive/name',views.EmpRetrive_Generic.as_view()),
    path('generic_update/<id>',views.EmpUpdate_Generic.as_view()),
    path('generic_delete/<id>',views.EmpDestroy_Generic.as_view()),
    path('generic_create_list/',views.EmpListCreate_Generic.as_view()),
    path('generic_retrive_update/<name>',views.EmpRetrive_Update.as_view()),
    path('generic_retrive_delete/<name>',views.EmpRetrive_Destroy.as_view()),
    path('generic_retrive_update_delete/<name>',views.EmpRetrive_Update_Delete.as_view()),
    path('password_forgot',views.user_send_email),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('new_password/<id>',views.new_password,name='new_password'),
    # path('emp_viewset',views.EmpViewset.as_view({'get':'list'}))

    
    
]

urlpatterns += router.urls
