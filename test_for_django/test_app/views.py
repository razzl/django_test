# #coding:utf-8
# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.

# def index(request):
# 	return HttpResponse(u"这只是一个简单的测试")
from django.shortcuts import render
from django.http import HttpResponse

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))