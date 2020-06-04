from django.db import models

from lib.base_model import MixinModel



class Other(models.Model, MixinModel):
    name = models.CharField(max_length=64, verbose_name='傻帽的名字')
    user_id = models.IntegerField(verbose_name='用户的ID')

    @property
    def user(self):
        from user.models import User
        if not hasattr(self ,'_user'):
            try:
                self._user =User.objects.get(pk=self.id)
            except User.DoesNotExist:
                return None
        return self._user