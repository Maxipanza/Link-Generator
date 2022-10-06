import datetime
#from polls.APIdolarOficial import claseDolar
#from polls.APIdolarOficial import apiFer
from secrets import choice
from time import time
from xmlrpc.client import boolean
from django.db import models
from django.utils import timezone
from django.contrib import admin

from polls.tucson import apiFer

# Create your models here.
class Question (models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('dia publicado')
    #valor_dolar_oficial = claseDolar().oficial()
    #valor_dolar_blue = claseDolar().blue()
    #apiFer()
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='publicado recientemente?'
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #valor_dolar_oficial_choice = claseDolar().oficial()
    #valor_dolar_blue_choice = claseDolar().blue()
    def __str__(self):
        return self.choice_text