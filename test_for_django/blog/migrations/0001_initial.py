# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('data_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('content', models.TextField(null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe')),
                ('tag_cn_name', models.CharField(max_length=50, verbose_name=b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe5\xad\x97', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', max_length=50, blank=True),
        ),
    ]
