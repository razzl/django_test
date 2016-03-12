from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from people.models import Person

def testdb(request):
    test1 = Person(name='razzl',age='8')
    test1.save()
    return HttpResponse("the data is save now!")