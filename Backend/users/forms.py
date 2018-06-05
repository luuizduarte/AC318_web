from django.forms import ModelForm
from .models import User

class UserForm (ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'weight', 'height', 'email', 'percentageFat', 'sickness', 'intolerance' ,'physicalActivity', 'medicines', 'sex']
