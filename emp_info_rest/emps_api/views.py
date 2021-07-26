from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from emps_api.models import EmpPersonal
from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EmpPersonal
from django.core import serializers
from django.contrib.auth.models import User
from .serializers import Empserializer


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


@api_view(['GET','PUT','DELETE'])
def get_single(request,id):
    try:
     emp_data = EmpPersonal.objects.get(id=id)
    except:
        return Response({"message": "user info doesnot Exist !"})
    if request.method == "GET":
        ser_data = Empserializer(emp_data)
        print(ser_data)
        # data = {
        #             "name" : emp_data.name,
        #             "mobile" : emp_data.mobile,
        #             "email" : emp_data.per_email,
        #             "age":emp_data.age,
        #             "address" : emp_data.address,
        #             "country" :emp_data.country
        #         }   
        return Response(ser_data.data)
    elif request.method == "PUT":
        emp_data.name = request.data.get('name')
        emp_data.mobile = request.data.get('mobile')
        emp_data.per_email = request.data.get('email')
        emp_data.age = request.data.get('age')
        emp_data.address = request.data.get('address')
        emp_data.country = request.data.get('country')
        emp_data.save()
        return Response({"message":'data updated successfully !'})

    elif request.method == "DELETE":
        User.objects.get(id=emp_data.user.id)
        print(emp_data.user.id)
        User.objects.get(id = emp_data. user.id).delete()
        emp_data.delete()
        return Response({"message":"data deleted successfullt"})


@api_view(['PUT'])
def change_password(request,id):
    try:
        emp_data = EmpPersonal.objects.get(id=id)
    except:
        return Response({"message":"user info doesnot exist !"})
    if request.method == "PUT":
        password = request.data.get('password')
        confirm_password =request.data.get('confirm_password')
        if password == confirm_password:
            user_data = User.objects.get(id = emp_data.user.id)
            user_data.set_password(password)
            user_data.save()
            return Response({"message":"password is updated successfully"})
        else:
            return Response({"message":" password mismatched !"})
  

# class based views is of 3 types:
  # 1.APIVIEW
  # 2.Generic Api views
  # 3.Viwssets


class EmpersonalListView(APIView):
    def get(self,request):
        emp_data = EmpPersonal.objects.all()
        serializer = Empserializer(emp_data,many=True)
        return Response(serializer.data)

    def post(self,request):
        Serializer = Empserializer(data=request.data)
        if Serializer.is_valid():
            print(Serializer.data)
            user_data =User(username=Serializer.data.get("name"),email = Serializer.data.get("per_email"),is_active = True,is_staff= True)
            user_data.set_password(request.data.get("passsword"))
            user_data.save()
            EmpPersonal.objects.create(name=Serializer.data.get("name"),mobile = Serializer.data.get("mobile"),per_email =Serializer.data.get("per_email"),age =Serializer.data.get("age"),address=Serializer.data.get("address"),country=Serializer.data.get("country"),user=user_data)
            return Response({"message":"Register successfully"})
        return Response({"message":"validations missing"})

class EmpersonalDetailView(APIView):
    def get(self,request,id):
        emp_data = EmpPersonal.objects.get(id=id)
        Serializer = Empserializer(emp_data)
        return Response(Serializer.data)
     
    def put(self,request,id):
        emp_data = EmpPersonal.objects.get(id=id)
        Serializer = Empserializer(emp_data,data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response({"message":"put method"})
    
    def delete(self,request,id):
        emp_data = EmpPersonal.objects.get(id=id)
        User.objects.get(id=emp_data.user.id).delete()
        emp_data.delete()
        return Response({"message":"user deleted successfully"})
      
