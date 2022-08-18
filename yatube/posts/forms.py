from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {
            'text': 'Текст записи',
            'group': 'Группы',
        }
        help_texts = {
            'text': ('Поле для ввода вашей записи.'),
            'group': ('Группа к которой относится запись.'),
        }
