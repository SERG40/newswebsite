# Generated by Django 4.1 on 2022-08-05 10:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0008_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
