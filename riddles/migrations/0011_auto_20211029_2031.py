# Generated by Django 3.2.8 on 2021-10-29 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0010_auto_20211029_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 29, 20, 31, 46, 610579)),
        ),
        migrations.AlterField(
            model_name='riddle',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Картинка'),
        ),
    ]