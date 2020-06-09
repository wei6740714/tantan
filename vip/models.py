from django.db import models

# Create your models here.


class Vip(models.Model):
    name=models.CharField(max_length=32,verbose_name='VIP名字',unique=True)
    level=models.IntegerField(verbose_name='VIP等级',unique=True)

    @property
    def permissions(self):
        if not hasattr(self,'_permissions'):
            vip_permissions=VipPermission.objects.filter(vip_id=self.id)
            vip_permission_ids=[vip_permission.permission_id for vip_permission in vip_permissions]
            self._permissions=Permission.objects.filter(id__in=vip_permission_ids)
        return self._permissions




class Permission(models.Model):
    name=models.CharField(max_length=32,verbose_name='权限名字',unique=True)
    description=models.CharField(max_length=64,verbose_name='权限描述')

class VipPermission(models.Model):
    vip_id=models.IntegerField(verbose_name='Vip ID')
    permission_id=models.IntegerField(verbose_name='权限 ID')
