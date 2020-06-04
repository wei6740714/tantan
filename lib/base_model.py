

class MixinModel():
    def to_dict(self,ignore=()):
        fields=self._meta.fields
        result={}
        for field in fields:
            name=field.name
            if not name in ignore:
                result[name]=getattr(self,name)
        return result


