from django import forms

from .models import BlogPost


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Заголовок', 'text':'Текст'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,  # Увеличить высоту поля
            }),
        }