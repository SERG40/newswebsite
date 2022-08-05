
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class News(models.Model):
    """Модель News (дата новости, заголовок новости, текст новости, автор)"""
    title = models.CharField(max_length=255, verbose_name='Заголовок новости')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now='True', verbose_name='Дата новости')
    likes = models.ManyToManyField(User, related_name='blog_post')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name='Автор'
    )

    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Нововсти'
        ordering = ['-pub_date']


class Comment(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("date published", auto_now_add=True)

    def total_comment(self):
        return self.post.count()

    def __str__(self):
        return self.text
