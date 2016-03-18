from django.db import models

# Create your models here.
class Sql_test_user(models.Models):
    user_name = models.CharField(max_length=200)
    user_passwd = models.CharField(max_length=200)
    user_age = models.IntegerField(default=0)
