from .models import News, Comment
from django import forms


class CreateNewsForm(forms.ModelForm):
    """Форма создания новости."""

    class Meta:
        """Выбираем поля."""

        model = News
        fields = '__all__'

        widgets = {
            'text': forms.Textarea(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        labels = {'text': 'Добавить комментарий'}
        help_texts = {'text': 'Текст комментария'}