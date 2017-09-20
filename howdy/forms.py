from django import forms

from .models import Address

class PostForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('name', 'email',)