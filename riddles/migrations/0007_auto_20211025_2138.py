# Generated by Django 3.2.8 on 2021-10-25 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0006_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='option',
        ),
        migrations.AddField(
            model_name='answers',
            name='answers',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='answers',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 21, 38, 26, 549347)),
        ),
    ]