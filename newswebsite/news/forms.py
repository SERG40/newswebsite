from .models import News, Comment
from django import forms


class CreateNewsForm(forms.ModelForm):
    """Форма создания новости."""

    class Meta:
        """Выбираем поля."""

        model = News
        fields = ('author', 'title', 'text', )

        widgets = {
            'text': forms.Textarea(),
        }


class CommentForm(forms.ModelForm):
    """Форма создания коментария."""
    class Meta:
        model = Comment
        fields = ('text', )
        labels = {'text': 'Добавить комментарий'}
        help_texts = {'text': 'Текст комментария'}
