from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        label = {
            'text': 'Текст записи',
            'group': 'Группа',
        }
        help_texts = {
            'text': ('Поле для ввода вашей записи.'),
            'group': ('Группа к которой относится запись.'),
        }
