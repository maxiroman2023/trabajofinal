# Generated by Django 3.2.6 on 2023-07-28 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0003_alter_articles_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='user',
        ),
    ]