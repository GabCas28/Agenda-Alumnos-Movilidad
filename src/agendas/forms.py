from django.forms import ModelForm, Form, CharField, FileField
from .models import Agenda, Category

class AgendaForm(ModelForm):
     class Meta:
         model = Agenda
         fields = '__all__'

class CategoryForm(ModelForm):
     class Meta:
         model = Category
         fields = '__all__'