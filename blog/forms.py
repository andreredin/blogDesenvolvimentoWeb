from django import forms
from .models import Post, comentario


class formComentario(forms.ModelForm):

    class Meta:
        model = comentario
        fields = ('texto',)


class formPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo','texto', 'data_publicacao')
        widgets = {
            'data_publicacao': forms.DateTimeInput(attrs={'class': 'datetimepicker'}),
        }