from django.shortcuts import render
from sql_injection.models import Sql_test_user
from django.http import HttpResponse
from django.db import connection
# Create your views here.

def get_user(request):
    name = request.GET['name']
    # user = Sql_test_user.objects.get(user_name = name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  sql_injection_sql_test_user WHERE user_name = name")
    user = [row[0] for row in cursor.fetchall()]
    return HttpResponse('username:'user[user_name]+'\n'+'user password:'+user[user_passwd])