# Generated by Django 3.2.6 on 2023-07-31 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=254)),
                ('message_body', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
