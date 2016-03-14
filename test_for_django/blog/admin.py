from django.contrib import admin
from blog.models import Tag,Article
# Register your models here.

admin.site.Register(Tag)
admin.site.Register(Article)