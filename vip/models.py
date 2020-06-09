from django.db import models

# Create your models here.


class Vip(models.Model):
    name=models.CharField(max_length=32,verbose_name='VIP名字',unique=True)
    level=models.IntegerField(verbose_name='VIP等级',unique=True)

class Permission(models.Model):
    name=models.CharField(max_length=32,verbose_name='权限名字',unique=True)
    description=models.CharField(max_length=64,verbose_name='权限描述')

class VipPermission(models.Model):
    vip_id=models.IntegerField(verbose_name='Vip ID')
    permission_id=models.IntegerField(verbose_name='权限 ID')
