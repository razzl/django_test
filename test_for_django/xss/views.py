from django.shortcuts import render
# from sql_injection.models import Sql_test_user
from django.http import HttpResponse
from django.db import connection
# Create your views here.
from django.template import Context, Template
import re
def xss_1(request):
    name = request.GET['name']
    t = Template('<h2>if you input something, it will show on the page:{{ name|safe }}</h2>')
    c = Context({'name': name})
    return HttpResponse(t.render(c))

def xss_2(request):
    name = request.GET['name']
    name = re.sub(r'script','',name)
    t = Template('<h2>if you input something, it will show on the page:{{ name|safe }}</h2>')
    c = Context({'name': name})
    return HttpResponse(t.render(c))
# Create your views here.
