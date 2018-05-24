from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        field = ['name', 'age', 'weight', 'height', 'email', 'percentageFat', 'sickness', 'intolerance' ,'physicalActivity', 'medicines', 'sex']
