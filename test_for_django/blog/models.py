# -*- coding: utf-8 -*-
from django.db import models

# class Person(models.Model):
#     name = models.CharField('姓名'，max_length=50)
#     age = models.IntegerField('年龄'，blank=True)

#     def __unicode__(self):
#         return self.name
class Tag(models.Model):
    tag_name = models.CharField('标签',max_length=50)
    tag_cn_name = models.CharField('中文名字',max_length=50,blank=True)

    def __unicode__(self):
        return self.tag_name

class Article(models.Model):
    title = models.CharField('标题',max_length=100)
    tag = models.ManyToManyField(Tag,max_length=50,blank=True)
    data_time = models.DateTimeField('日期',auto_now_add=True)
    content = models.TextField('内容',blank=True,null=True)

    def __unicode__(self):
        return self.title

        class Meta:
            verbose_name = '文章'
            verbose_name_plural = '文章'
            ordering = ['-date_time']