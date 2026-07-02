class Myclass1:
    def fun1(self):
        
        print("Method 1!!")
        
        
class Myclass2:
    def fun1(self):
        super().fun1()
        print("method 2!!")
        

class Myclass3(Myclass2,Myclass1):
    def fun1(self):
        super().fun1()
        print("Method 3!!")
        
        
obj =Myclass3()
obj.fun1()