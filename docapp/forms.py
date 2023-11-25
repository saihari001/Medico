from django import forms
from .models import ImageGallery

class UploadFiles(forms.ModelForm):
    class Meta:
        model=ImageGallery
        fields=("title","image","video")
        
    