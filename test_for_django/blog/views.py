from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article,Tag
# Create your views here.

def home(request):
    # return HttpResponse("<label style='color: ff0000'>Hello World</label>")
    post_list = Article.objects.all()
    return render(request,'index.html')
def get_articles(request,tag_name):
    posts = Article.objects.filter(tag_tag_name = tag_name)
    return render(request,'idex.html',{'post_list':post_list})
def detail(request,id):
    post = Article.objects.get(id = str(id))
    return render(request,'index.html',{'post':post})