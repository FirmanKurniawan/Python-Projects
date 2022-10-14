#Constructor overloading
''' "a=1" : public variable
    "_a=1" : protected variable
    "__a=1 : private variable '''
class Sample:
    __a=None
    __b=None
    def __init__(self,a=0,b=0):
        self.__a=a
        self.__b=b
    def show(self):
        print(self.__a,self.__b)


obj1 = Sample()
obj2 = Sample(1)
obj3 = Sample(1,5)
obj4 = Sample(4,1.6)

obj1.show()
obj2.show()
obj3.show()
obj4.show()
# print(obj4.__a)
