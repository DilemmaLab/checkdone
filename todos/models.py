#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Todo(models.Model):
    text = models.CharField(blank=False, max_length=100, verbose_name='Task text') # (REQUIRED)
    deadline = models.DateTimeField(blank=False, verbose_name='Deadline') #  (REQUIRED) Or DateField(), if only Date is in Use.
    check = models.BooleanField(blank=False, default=False, verbose_name='Done?') # (REQUIRED)
    '''---'''
    donedate = models.DateTimeField(blank=True, null=True, verbose_name='Date, when done') # (Not nessessary) Or DateField(), if only Date is in Use.
    progress = models.FloatField(blank=False, default=0.0, verbose_name='Progress') # (Not nessessary) % for progressbar.
    textexp = models.TextField(blank=True, verbose_name='Expanded text explaination') # (Not nessessary) Detailed description of the task with topic, setted up in 'text'.

# ---------------------------------------------------------------------------------------------------------------------------------- #
''' (Not Implemented Yet) '''
'''class User(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='/tmp')
    
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    session <and etc. from django_db, ...>
    relations with Todo-Model: <->> to Todo-model (one-to-many)'''
