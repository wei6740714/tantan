from django.core.cache import cache
from django.db.models import QuerySet
from functools import wraps

def get_cached(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        pk=kwargs.get('id') or kwargs.get('pk')
        if pk and len(kwargs)==1:
            obj=cache.get(f'Model:{self.model.__name__}:{pk}',None)
            if not obj:
                obj=func(self,*args,**kwargs)
                cache.set(f'Model:{self.model.__name__}:{pk}',obj)

            return obj
        return func(self,*args,**kwargs)
    return  wrapper

def create_cached(func):
    @wraps(func)
    def wrapper(self, **kwargs):
        obj=func(self,**kwargs)
        cache.set(f'Model:{self.model.__name__}:{obj.pk}',obj)
        return obj
    return  wrapper

QuerySet.get=get_cached(QuerySet.get)
QuerySet.create=create_cached(QuerySet.create)

#QuerySet.get_or_create不用重写,查看源代码可知,它依然调用的是get和create方法



