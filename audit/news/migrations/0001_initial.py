# Generated by Django 5.1.3 on 2024-11-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('date', models.DateField(verbose_name='Дата')),
                ('text', models.TextField(verbose_name='Новость')),
            ],
        ),
    ]
