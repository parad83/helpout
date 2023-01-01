from atexit import register
from tkinter.tix import Tree
from unittest import case
from django import template
from datetime import datetime, timezone


register = template.Library()

@register.filter
def time_since(date):
    delta = datetime.now(timezone.utc)-date
    if delta.days < 1:
        return str('today at {}'.format(date.strftime('%H:%M')))
    elif delta.days < 2:
        return str('yesterday at {}'.format(date.strftime('%H:%M')))
    else:
        return str(date.strftime('%d/%m/%Y'))

@register.filter
def addstr(arg1, arg2):
    return str(arg1) + str(arg2)