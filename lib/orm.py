from django.core.cache import cache
from django.db.models import QuerySet
from functools import wraps

def get_cached(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        obj=cache.get(f'{self}',None)
        print('********',self)
        if not obj:
            obj=func(self,*args,**kwargs)
            cache.set(f'{self}',obj)
            print('func.get')
        print(self,'get from cached')
        return obj
    return  wrapper


QuerySet.get=get_cached(QuerySet.get)



