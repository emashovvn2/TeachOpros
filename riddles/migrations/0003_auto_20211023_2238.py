# Generated by Django 3.2.8 on 2021-10-23 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0002_riddle_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='riddle',
            options={'verbose_name': 'Номер вопроса'},
        ),
        migrations.AlterField(
            model_name='riddle',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Номер вопроса'),
        ),
    ]