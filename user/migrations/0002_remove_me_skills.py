# Generated by Django 4.1.6 on 2023-06-13 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='me',
            name='skills',
        ),
    ]