from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from .forms import EmpPersonalModelForm,EmpPersonalForm
from .models import EmpPersonal
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
from django.views import View
from django.views.generic import CreateView,ListView,UpdateView
from django.urls import reverse_lazy
import pdb


# Create your views here.

def user_register(request):
    return HttpResponse("you are successfully Registered with us.")

def basic_load(request):
    return render(request,'basic.html')

def user_model_form(request):
    form = EmpPersonalModelForm()
    print(form)
    if request.method == "POST":
        save_form = EmpPersonalModelForm(request.POST)
        if save_form.is_valid:
          save_form.save()
        else:
            return HttpResponse("Invalid data!")
    return render(request,'model_forms.html',{'form':form})

def user_form(request):
    form = EmpPersonalForm()
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        per_email = request.POST.get('per_email')
        age = request.POST.get('age')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        print(name,mobile,per_email,age,address,gender,country)
        emp_info =EmpPersonal(name=name,mobile=mobile,per_email=per_email,age=age,address=address,gender=gender,country=country)
        emp_info.save()
        return HttpResponse("Registered successfully")
    return render (request,'form.html',{'form':form})

def user_html_form(request):
    if request.method == "POST":
        # print(request.POST)
        # print(request.FILES)
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        per_email = request.POST.get('per_email')
        age = int(request.POST.get('age'))
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        photo = request.FILES.get('photo')
        user_data = User.objects.create(username=name,email=per_email,is_active=True,is_superuser=True,is_staff=True)
        user_data.set_password(password)
        user_data.save()
        messages.success(request,"User added successfully")
        EmpPersonal.objects.create(name=name,mobile=mobile,per_email=per_email,age=age,address=address,gender=gender,country=country,user=user_data,profile_pic =photo)
    return render(request,'html_form.html')

def get_user_list(request):
    all_data = {}
    if request.user.is_authenticated:
        if request.user.is_superuser:
         all_data = EmpPersonal.objects.all()
        else:
           all_data = EmpPersonal.objects.filter(user=request.user)
    return render(request,'all_data.html',{'data':all_data})

def get_single_data(request,id):
    get_data = EmpPersonal.objects.get(id=id)
    return render(request,'single_data.html',{'data':get_data})

def update_data(request,id):
    get_data = EmpPersonal.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        per_email = request.POST.get('per_email')
        age = int(request.POST.get('age'))
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        filter_data = EmpPersonal.objects.filter(id=id)
        filter_data.update(name=name,mobile=mobile,per_email=per_email,age=age,address=address,gender=gender,country=country)
        return HttpResponse("updated successfully")
    return render(request,'update_data.html',{'data':get_data})


def delete_user(request,id):
    EmpPersonal.objects.get(id=id).delete()
    messages.success(request,"user deleted successfully")
    return redirect('get_user_list')

def user_login(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        check_user =authenticate(username=username,password=password)
        if check_user:
            login(request,check_user)
            messages.success(request,"Hi {} you are logged in successfully".format(check_user))
            return redirect("get_user_list")
        else:
            messages.warning(request,"Invalid credentials try again")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')

def user_send_email(request):
    if request.method == "POST":
        email = request.POST ['email']
        email_check = User.objects.filter(email=email)
        if email_check:
            otp_save  = EmpPersonal.objects.filter(per_email=email)
            otp = random.randint(1000,9999)
            save_data = otp_save[0]
            save_data.otp = str(otp)
            save_data.save()
            msg= "Hi {},\n you have requested for a forgot password feature please use the below code for verification {}".format(email_check[0].username,otp)
            send_mail('password change verification code',msg,settings.EMAIL_HOST_USER ,[email_check[0].email])
            return redirect('verify_otp')
        else:
            messages.warning(request,'Email id is incorrect!')
    return render(request,'send_email.html')

def verify_otp(request):
    if request.method == "POST":
        gen_otp = request.POST['otp']
        check_otp = EmpPersonal.objects.filter(otp=gen_otp)
        if check_otp:
            return redirect('new_password',id=check_otp[0].id)
        else:
            messages.warning(request,'please enter correct OTP')

    return render(request,'verify_otp.html')

def new_password(request,id):
    emp_info = EmpPersonal.objects.get(id=id)
    if request.method == "POST":
        password = request.POST['password']
        check_email = emp_info.per_email
        user_data = User.objects.get(email= check_email)
        user_data.set_password(password)
        user_data.save()
        return redirect('user_login')
    return render(request,'new_password.html')


class HelloSample(View):# get,post, update, delete
    def get(self,request):
        return HttpResponse("Hello World!")
    
# Generic views -- CreateView,ListView,DetailView, UpdateView,DeleteView

class EmpPersonal_cls(CreateView):
    model = EmpPersonal
    # fields = "__all__"
    fields = ("name","mobile","per_email","age","address","gender","country","profile_pic") 
    success_url = reverse_lazy('hello_cls')
    def form_valid(self, form):
        # pdb.set_trace()
        name = form.data.get('name')
        per_email = form.data.get('per_email')
        password = form.data.get('password')

        user_data = User.objects.create(username=name,email=per_email,is_active=True,is_superuser=True,is_staff=True)
        user_data.set_password(password)
        user_data.save()

        form_data = form.save(commit = False)
        form_data.user = user_data
        form_data.save()
        return super().form_valid(form)


class EmpPersonal_List(ListView):
    model = EmpPersonal


class EmpPersonal_Update(UpdateView):
    model = EmpPersonal
    fields = ("name","mobile","per_email","age","address","gender","country","profile_pic")
    success_url = reverse_lazy('hello_cls')

class EmpPersonal_Delete(DeleteView):
    model = EmpPersonal
    success_url = reverse_lazy('hello_cls')

class EmpPersonal_Details(DetailView):
    model = EmpPersonal