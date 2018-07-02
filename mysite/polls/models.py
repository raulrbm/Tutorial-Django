# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

#Tabla que contiene los formularios del administrador
class adminForm(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

#Tabla con los campos de seleccion simple para el form del admin
class adminSChoice(models.Model):
    formulario = models.ForeignKey(adminForm, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    place = models.IntegerField(default=0)
    other = models.BooleanField() 
    label = models.CharField(max_length=50) 
    txt = models.CharField(max_length=500) 
    def __str__(self):
        return self.name

#Tabla con los distintos campos de opciones para seleccion simple
class sChoices(models.Model):
    sChoice = models.ForeignKey(adminSChoice, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)
    def __str__(self):
        return self.choice_text

#Tabla con los campos de seleccion multiple para el form del admin
class adminMChoice(models.Model):
    formulario = models.ForeignKey(adminForm, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    place = models.IntegerField(default=0)
    other = models.BooleanField() 
    label = models.CharField(max_length=50) 
    txt = models.CharField(max_length=500) 
    def __str__(self):
        return self.name

#Tabla con los distintos campos de opciones para seleccion multiple
class mChoices(models.Model):
    mChoice = models.ForeignKey(adminMChoice, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)
    def __str__(self):
        return self.choice_text

#Tabla con los distintos campos de textfields para el form del admin
class adminTextF(models.Model):
    formulario = models.ForeignKey(adminForm, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    place = models.IntegerField(default=0)
    label = models.CharField(max_length=50) 
    txt = models.CharField(max_length=50) 
    def __str__(self):
        return self.name

#Tabla con los distintos campos de text areas para el form del admin
class adminTextA(models.Model):
    formulario = models.ForeignKey(adminForm, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    place = models.IntegerField(default=0)
    label = models.CharField(max_length=50) 
    txt = models.CharField(max_length=500) 
    def __str__(self):
        return self.name

#Tabla con los distintos campos de text areas para el form del admin
class adminBool(models.Model):
    formulario = models.ForeignKey(adminForm, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    place = models.IntegerField(default=0)
    boolean = models.BooleanField()
    def __str__(self):
        return self.name