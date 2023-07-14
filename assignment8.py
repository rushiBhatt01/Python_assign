class A:
    def __init__(self,a,b,c):
        self.__a=a
        self._b=b
        self.c=c


class B(A):

    def display(self):
        try:
            print("Accessing private member:")
            print(f"a: {self.__a}")  
        except AttributeError:
            print("Error: Private member cannot be accessed.")
        finally:
            print(f"b:{self._b}, c:{self.c}")
b=B(10,20,30)
b.display()

