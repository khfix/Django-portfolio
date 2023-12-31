# Generated by Django 4.1.6 on 2023-06-12 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='photos/')),
                ('about', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('cv', models.FileField(upload_to='cv/')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='project.programminglang')),
            ],
        ),
    ]
