# Generated by Django 3.2.8 on 2021-10-29 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0012_auto_20211029_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 29, 22, 30, 37, 245276)),
        ),
        migrations.AlterField(
            model_name='riddle',
            name='image',
            field=models.ImageField(blank=True, upload_to='riddles/static', verbose_name='Картинка'),
        ),
    ]
