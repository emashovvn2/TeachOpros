# Generated by Django 3.2.8 on 2021-10-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='riddle',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]