#!/usr/bin/python
# -*- coding: utf-8 -*-
#import unittest
from django.utils import unittest
from todos.models import Todo
from todos.forms import AddNewForm
from todos.views import add_new

class ModelsTestCase(unittest.TestCase):
    def modelTodoTestBasic(self):
        self.model = Todo.objects.create(text='This is to test adding of new items=records', deadline='2006-10-25 14:30:59', progress='0.0')

class FormsTestCase(unittest.TestCase):
    def formAddNewFormTestBasic(self):
        form_data = {'text': 'This is to test adding of new items=records', 'deadline': '2006-10-25 14:30:59', 'progress': '0.0'}
        form = AddNewForm(data=form_data)
        self.assertTrue(form.is_valid())
        #form.is_bound
        #form.errors
        #form.cleaned_data

class ViewsTestCase(unittest.TestCase):
    def viewadd_newTestBasic(self):
        request = ['This is to test adding of new items=records', '', '']
        self.assertEqual(add_new(request, 0), 'This is to test adding of new items=records')
        self.assertEqual(add_new(request, 1), '')
