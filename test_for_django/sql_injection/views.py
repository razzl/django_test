from django.shortcuts import render
from sql_injection.models import Sql_test_user
from django.http import HttpResponse
# Create your views here.

def get_user(request,name):
    user = Sql_test_user.objects.filter(user_name = name)
    return HttpResponse("user.user_name  user.user_passwd")