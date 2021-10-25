from django.db import models
from datetime import datetime

class Riddle(models.Model):
    ###Вопросы###
    name = models.CharField('Номер вопроса',max_length=255, default='')
    riddle_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Option(models.Model):
    ###Ответы###
    riddle = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.riddle) + ' - ' + self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class Answers(models.Model):
    ###Ответы###
    riddle = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    answers = models.TextField(null=True)
    date = models.DateTimeField(default=datetime.now())
    ip = models.CharField(max_length=12)

    def __str__(self):
        return str(self.riddle) + ' - ' + self.option

    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'

# Create your models here.
