
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmpPersonal(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    per_email = models.CharField(max_length=30)
    age = models.IntegerField(max_length=2)
    address = models.TextField()
    gender = models.CharField(max_length=6)
    country = models.CharField(max_length=20,default='india')
    otp = models.CharField(max_length=6,default='000000')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to='media',default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'personal_info'