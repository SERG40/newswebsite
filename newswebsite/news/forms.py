from .models import News
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
