from emps_api.models import EmpPersonal
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EmpPersonal
from django.core import serializers
from django.contrib.auth.models import User

# Create your views here.


@api_view(['GET', 'POST'])
def hello_api(request):
    if request.method == 'GET':
       return Response({'message':'Hello World !'})
    elif request.method == 'POST':
        print(request)
        return Response(request.data)

@api_view(['GET', 'POST'])
def get_data(request):
    if request.method == 'GET':
        emp_data = EmpPersonal.objects.all()
        emp_data_value = []
        for ele in emp_data:
            data = {
                "name" : ele.name,
                "mobile" : ele.mobile,
                "email" : ele.per_email,
                "age":ele.age,
                "address" : ele.address,
                "country" :ele.country
            }    
            emp_data_value.append(data)
        return Response(emp_data_value)
    elif request.method == 'POST':
        print(request.data)
        user_data =User(username=request.data.get("name"),email = request.data.get("email"),is_active = True,is_staff= True)
        user_data.set_password(request.data.get("passsword"))
        user_data.save()
        EmpPersonal.objects.create(name=request.data.get("name"),mobile = request.data.get("mobile"),per_email =request.data.get("email"),age =request.data.get("age"),address=request.data.get("address"),country=request.data.get("country"),user=user_data)
        request.data.remove('password')
        return Response(request.data)


@api_view(['GET'])
def get_single(request,id):
    emp_data = EmpPersonal.objects.get(id=id)
    data = {
                "name" : emp_data.name,
                "mobile" : emp_data.mobile,
                "email" : emp_data.per_email,
                "age":emp_data.age,
                "address" : emp_data.address,
                "country" :emp_data.country
            }   
    return Response(data)