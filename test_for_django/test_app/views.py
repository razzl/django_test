###################################################
# #coding:utf-8
# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.

# def index(request):
# 	return HttpResponse(u"这只是一个简单的测试")
###################################################
# from django.shortcuts import render
# from django.http import HttpResponse

# def add(request):
#     a = request.GET['a']
#     b = request.GET['b']
#     c = int(a) + int(b)
#     return HttpResponse(str(c))
# def add2(request,a,b):
#     c = int(a) + int(b)
#     return HttpResponse(str(c))
###################################################
# from django.shortcuts import render

# def home(request):
#     return render(request,'home.html')
###################################################
# -*- coding: utf-8 -*-
# from django.shortcuts import render

# def home(request):
#     string = u"It is only a test for learning django.(这只是一个简单的测试)"
#     return render(request,'home.html',{'string':string})
# ###################################################
# from django.shortcuts import render

# def home(request):
#     TutoriaList = ["html","css","jquery","python"]
#     return render(request,'home.html',{'TutoriaList':TutoriaList})
###################################################
from django.shortcuts import render

def home(request):
    List = map(str,range(100))
    return render(request,'home.html',{'List':List})
def add(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))