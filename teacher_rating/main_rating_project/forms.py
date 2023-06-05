from .models import EnteringPerson
from django.forms import ModelForm, TextInput, Select


class EnteringPersonForm(ModelForm):
    class Meta:
        model = EnteringPerson
        fields = [
            'unique_numbers',
            'full_name',
            'role'
        ]

        widgets = {
            "unique_numbers": TextInput(
                attrs={
                    'class': 'form',
                    'placeholder': 'Пароль'
                }
            ),
            "full_name": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Логин'
            }),
            "role": Select(
                attrs={
                    'class': 'form',
                    'placeholder': 'Роль'
                 },
                choices=[
                    ('student', "Студент"), 
                    ('teacher', "Преподаватель"), 
                    ('matriculant', "Абитуриент"), 
                    ('director', "Руководитель")
                ]
            ),
            
        }

        
