# Generated by Django 4.2.2 on 2024-01-24 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
    ]
