from django.shortcuts import render
from sql_injection.models import Sql_test_user
from django.http import HttpResponse
from django.db import connection
# Create your views here.
import re
def get_user(request):
    name = request.GET['name']
    # user = Sql_test_user.objects.get(user_name = name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  sql_injection_sql_test_user WHERE user_name ="+"'" + name+"'")
    user = cursor.fetchall()
    return render(request,'sql_test_user.html',{'user':user})
    # return HttpResponse(user[0][1])
def get_user_2(request):
    name = request.GET['name']
    # user = Sql_test_user.objects.get(user_name = name)
    for i in name:
        if i.isspace():
            return HttpResponse("<h2>There is some spaces in your string!</h2>")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  sql_injection_sql_test_user WHERE user_name ="+"'" + name+"'")
    user = cursor.fetchall()
    return render(request,'sql_test_user.html',{'user':user})
def get_user_3(request):
    userid = request.GET['id']
    pattern = re.compile(r'^\d+$',re.M)
    if pattern.match(userid)!=True:
        return HttpResponse("<h2>Your input id is not a integer!</h2>")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  sql_injection_sql_test_user WHERE id =" + userid)
    user = cursor.fetchall()
    return render(request,'sql_test_user.html',{'user':user})