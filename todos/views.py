#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q # Q-objects for complex search/lookups
from time import strptime
from datetime import datetime
from .models import Todo
from .forms import AddNewForm
from django.template.context_processors import csrf
from django.template import RequestContext
#from django.conf import settings # To fix Search for cyrillyc symbols inside not-set_to_utf8 DB MySQL
# For delete_id #
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
# For delete_id #
from django.utils import timezone

#from django.views.defaults import page_not_found


def index(request):
    return render_to_response('basic/index.html')

#@csrf_protect
def add_new(request):
    if request.method == 'POST':
        form = AddNewForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['check']==True:
                form.cleaned_data['progress']=100.0
                if form.cleaned_data['donedate']==None:
                    form.cleaned_data['donedate']=datetime.now().strftime("%Y-%m-%d %H:%M")
            elif form.cleaned_data['progress']==100.0:
                form.cleaned_data['check']=True
                if form.cleaned_data['donedate']==None:
                    form.cleaned_data['donedate']=datetime.now().strftime("%Y-%m-%d %H:%M")
            elif form.cleaned_data['progress']==None:
                form.cleaned_data['progress']=0.0
            # ?? Not works, but why?
            '''else:
                if form.cleaned_data['donedate']:
                    form.cleaned_data['check']=True
                    form.cleaned_data['progress']=100.0
                    #??
                if form.cleaned_data['donedate']!=None:
                    form.cleaned_data['check']=True
                    form.cleaned_data['progress']=100.0'''
            '''if form.cleaned_data['donedate']!=None:
                form.cleaned_data['check']=True
                form.cleaned_data['progress']=100.0
            if form.cleaned_data['donedate']:
                form.cleaned_data['check']=True
                form.cleaned_data['progress']=100.0
            if not(form.cleaned_data['donedate']==None):
                form.cleaned_data['check']=True
                form.cleaned_data['progress']=100.0'''
            # ?? Not works, but why?
            if form.cleaned_data['donedatepk']==None:
                pass
            else:
                form.cleaned_data['check']=True
                form.cleaned_data['progress']=100.0
            Todo.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/todo/', RequestContext(request, {'form': form}))
    else:
        form = AddNewForm()
    return render_to_response('add.html', {'form': form}, context_instance=RequestContext(request, {'form': form}))

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        month_int=0
        try:
            month_int=strptime(q,'%B').tm_mon
        except ValueError:
            pass
            #month_int=0
        #cs = settings.DEFAULT_CHARSET.replace('-', '') # To fix Search for cyrillyc symbols inside not-set_to_utf8 DB MySQL
        #cursor.execute("set character set %s" % cs) # To fix Search for cyrillyc symbols inside not-set_to_utf8 DB MySQL
        todos = Todo.objects.filter(Q(id__icontains=q) |
                                    Q(text__icontains=q) | Q(deadline__icontains=q)|
                                    Q(textexp__icontains=q)| Q(donedate__icontains=q)|
                                    Q(progress__icontains=q)| Q(deadline__month__icontains=month_int)|
                                    Q(pk__icontains=q))
        #month_int=Todo.objects.filter(donedate__year=q)[0]
        return render_to_response('search_results.html', {'todos': todos, 'query': q})
        #return HttpResponse(month_int)
    else:
        return HttpResponse('Please submit a search term.')

def show_all(request):
    #''' Show all todos '''
    #todos = Todo.objects.all().order_by('deadline')
    #todos = Todo.objects.all().order_by('-deadline')
    todos = Todo.objects.all().order_by('-id')
    if request.method == 'POST':
        form = AddNewForm(request.POST)
    else:
        form = AddNewForm()
    return render_to_response('todo.html', {'todos':todos, 'form': form}, context_instance=RequestContext(request, {'form': form}))

def delete_id(request, id):
    try:
        todo = get_object_or_404(Todo, pk=id).delete()
    except Http404:
        return HttpResponse(no_page(request))
    return HttpResponseRedirect('/todo/', RequestContext(request))

def check_id(request, id):
    '''todos = get_object_or_404(Todo, pk=id).update() # Weird, but caused in Error 'Todo object doesn't have attribute update()'
    return HttpResponseRedirect(reverse('todos.views.todos'))'''
    try:
        todo = get_object_or_404(Todo, pk=id)
        if todo.id:
            todo.check="True"
            todo.donedate=timezone.now()
            todo.progress=100
            todo.save(update_fields=['check', 'donedate', 'progress'])
            #Todo.objects.get(pk=todo.id).save(update_fields=['check', 'donedate', 'progress'])
    except Http404:
        return http_error(request)
        #return HttpResponse(no_page(request))
    return HttpResponseRedirect('/todo/', RequestContext(request))

def no_page(request):
    #''' 404 Page Not Found Custom Template '''
    return render_to_response('wrongpage404.html', {'url': request.build_absolute_uri})

# HTTP Error 404
def http_error(request):
    response = render_to_response(
    'wrongpage404.html',
    context_instance=RequestContext(request)
    )
    response.status_code = 404
    return response
# Universal HTTP Error
# Can be used as following:
# 404: views.http_error(request, 404)
# 500: views.http_error(request, 500)
# and etc.
'''def http_error(request, status):
    response = render_to_response(
    'wrongpage%s.html' % status,
    context_instance=RequestContext(request)
    )
    response.status_code = status
    return response'''

# Revrites Default 404-Page handler
# -- Can be used instead of http_error(request) 
# -- Can be used without anything inside urls.py-patterns
'''def handler404(request):
    response = render_to_response('404.html', {'url': request.build_absolute_uri},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response'''
# ---------------------------------------------------------------------------------------------------------------------------------- #
''' (Not Implemented Yet) '''
'''
def uncheck_item(request):
    return HttpResponse(message)
'''
'''
def sort_ascend(request, orderkey):
    orderkey = -orderkey
    return show_all(request, orderkey)

def sort_descend(request, orderkey):
    return show_all(request, orderkey)
'''
