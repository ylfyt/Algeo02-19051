from django import forms
from django.forms import ModelForm 
from django.forms import fields
from .models import FileUpload
from django.forms import ClearableFileInput

class FileUploadForm(ModelForm):
   class Meta:
      model = FileUpload
      fields = '__all__'
      widgets = {'uploadfile' : ClearableFileInput(attrs={'multiple': True}),}
