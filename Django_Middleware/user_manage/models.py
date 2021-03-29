from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=500,blank=False,null=False)
    mobile = models.CharField(unique=True, max_length=13,blank=False,null=False)
    password = models.CharField(max_length=500,blank=False,null=False)
    name = models.CharField(max_length=50)
    session = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
