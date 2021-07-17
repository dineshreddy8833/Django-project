from django.db.models import fields
from .models import EmpPersonal
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class EmpPersonalModelForm(forms.ModelForm):
    class Meta:
        model = EmpPersonal
        fields = "__all__"
class EmpPersonalForm(forms.Form):
     name = forms.CharField(max_length=20)
     mobile = forms.CharField(max_length=10)
     per_email = forms.CharField(max_length=25)
     age = forms.IntegerField()
     address = forms.CharField(max_length=20)
     gender = forms.CharField(max_length=6)
     country = forms.CharField(max_length=20)
    
     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.helper = FormHelper()
         self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('per_email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            
            Row(
                Column('mobile', css_class='form-group col-md-6 mb-0'),
                Column('age', css_class='form-group col-md-4 mb-0'),
                Column('gender', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'address',
            'country',
                       Submit('submit', 'submit')
        )

