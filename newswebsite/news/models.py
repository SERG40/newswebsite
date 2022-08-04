
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class News(models.Model):
    """Модель News (дата новости, заголовок новости, текст новости, автор)"""
    title = models.CharField(max_length=255, verbose_name='Заголовок новости')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now='True', verbose_name='Дата новости')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name='Автор'
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Нововсти'
        ordering = ['-pub_date']
