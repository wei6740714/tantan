
class A:
    def hello(self):
        print('A.hello')

def hello_cache(func):
    def wrapper(self,*args,**kwargs):
        print('wrapper',self)
        func(self,*args,**kwargs)
    return wrapper

A.hello=hello_cache(A.hello)

if __name__ == '__main__':
    a=A()
    a.hello()