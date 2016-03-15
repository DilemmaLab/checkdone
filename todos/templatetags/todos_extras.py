#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe
from datetime import datetime
from django.utils import timezone

register = template.Library()

# Insert your custom template tags and filters here.

@register.filter
def highlight(text, word):
    """
    Returns text-content with highlight.
    """
    month = ''
    if(isinstance(text, datetime)): # Whether text is a datetime?
        month = text.strftime('%m')
        text = text.strftime('%B %d, %Y, %H:%M:%S')
        '''elif (isinstance(text, char)):
            text=text.decode('ascii')
            text=text.encode('utf8')'''
    elif(isinstance(text, int)):
        text=str(text)
    elif(isinstance(text, long)):
        text=str(text)
    elif(isinstance(text, float)):
        text=str(text)
    text=text.decode('ascii')
    text=text.encode('utf8')

    begin_mark = 0
    end_mark = 0

    if word.lower() in text.lower():
        for i in word.lower():
            for j in text.lower()[end_mark:]:
                if i == j:
                    end_mark += 1
                    break
                else:
                    begin_mark += 1
                    end_mark += 1
                    continue

    text_to_replace = text[begin_mark:end_mark] # OK
    text = text.replace(text_to_replace, "<b>%s</b>" % text_to_replace) # OK

    if word.lower() in month.lower():
        begin_mark = 0
        end_mark = len(text.split(' ')[0])
        text_to_replace = text[begin_mark:end_mark] # OK
        text = text.replace(text_to_replace, "<b>%s</b>" % text_to_replace)

    return mark_safe(text)

@register.filter
def date_to_str(datevar, typevar):
    """
    Converts date to string for customization of Date-Format (used in search_result.html for cool reasons).
    """
    #strvar=datevar.strftime('%Y-%m-%d %H:%M:%S')
    if typevar:
        strvar=datevar.strftime('%B %d, %Y, %H:%M:%S')
    else:
        strvar=datevar.strftime('%d-%m-%Y, %H:%M:%S')
    return mark_safe(strvar)

@register.filter
def done_task(check, index):
    """
    Should be checkbox checked or uncheked?:-> (Whether task is done or Undone?)
    """
    div_class=''
    checked='unchecked'
    #disabled='False'
    disabled=''
    if check == True:
        div_class='striked-through'
        checked='checked'
        #disabled='True'
        disabled='disabled'
    list=[div_class, checked, disabled]
    return mark_safe(list[index])

@register.filter
def expired_task(deadline, check):
    now = timezone.now()
    expired_date=''
    #if deadline and check!='striked-through':
    if deadline and check!=True:
        if deadline<now:
            expired_date='expired_date'
    return mark_safe(expired_date)
