# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from people.models import Person

def testdb(request):
    # test1 = Person(name='razzl',age='8')
    # test1.save()
    # return HttpResponse("the data is save now!")
    response = ""
    response1 = ""
    data = Person.objects.all()
    #利用objects这个模型管理器的all获得所有的数据 相当于select * from ***
    response2 = Person.objects.filter(id=1)
    #filter 相当于sql中的where过滤条件
    response3 = Person.objects.get(id=1)
    #获取单个对象
    Person.objects.order_by('name')[0:2]
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    #数据排序
    Person.objects.order_by("id")
    
    # 上面的方法可以连锁使用
    Person.objects.filter(name="razzl").order_by("id")
    
    # 输出所有数据
    for var in data:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")