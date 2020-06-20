
class A:
    def hello(self):
        print('A.hello')

def hello_cache(func):
    def wrapper(self,*args,**kwargs):
        print('wrapper',self)
        func(self,*args,**kwargs)
    return wrapper

class B(A):
    def dog(self):
        print('dog')

A.hello=hello_cache(A.hello)



if __name__ == '__main__':
    b=B()
    print(b.__class__.__name__)
