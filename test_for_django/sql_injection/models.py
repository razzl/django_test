from django.db import models

# Create your models here.
class Sql_test_user(models.Model):
    user_name = models.CharField(max_length=200)
    user_passwd = models.CharField(max_length=200)
    user_age = models.IntegerField(default=0)
    def __unicode__(self):
        return self.user_name