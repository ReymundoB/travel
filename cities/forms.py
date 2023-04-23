from django import forms

from .models import Comment




class Commentform(forms.ModelForm):

    class Meta:
        model = Comment #indicamos el modelo del cual hereda, es el que realizamos

        fields=('text',)