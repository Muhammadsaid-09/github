from django.forms import *
from .models import *

class UserForm(ModelForm):
    class Meta:
        model=Users
        fields='__all__'

        widgets = {
            'name': TextInput(attrs={
                'style':'border-color:white; border-radius: 10px;',
                'placeholder':'Имя',
            }),
            'surname': TextInput(attrs={
                'style': 'border-color:white; border-radius: 10px;',
                'placeholder': 'Фамилия',
            }),
            'address': TextInput(attrs={
                'style': 'border-color:white; border-radius: 10px;',
                'placeholder': 'Адрес',
            }),
            'pol': Select(attrs={
                'style': 'border-color:white; border-radius: 10px;width:190px;height:30px',
            }),
        }
