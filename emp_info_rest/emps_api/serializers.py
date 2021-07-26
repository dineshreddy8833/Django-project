from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import EmpPersonal


class Empserializer(serializers.ModelSerializer):
    class Meta:
        model = EmpPersonal
        fields = ("name","mobile","per_email","age","address","country")