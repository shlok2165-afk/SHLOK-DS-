# Hybrid Inheritance 

# class Myclass1():
#     def fun1(self):
#         print("Method 1!!")
        
    
# class  Myclass2(Myclass1):
#     def fun1(self):
#         super().fun1()
#         print("Method 2!!")
        
        
# class  Myclass3(Myclass2):
#     def fun1(self):
#         super().fun1()
#         print("Method 3!!")


# class  Myclass4(Myclass2,Myclass3):
#     def fun1(self):
#         super().fun1()
#         print("Method 4!!")
        
        
        
# obj = Myclass4()
# obj.fun1( )



class Myclass1:
    def fun1(self):
        print("Method 1!!")
        
class Myclass2(Myclass1):
    def fun1(self):
        super().fun1()
        print("Method 2!!")
        
class Myclass3(Myclass2):
    def fun1(self):
        super().fun1()
        print("Method 3!!")

# FIX: Order change kari
class Myclass4(Myclass3, Myclass2):
    def fun1(self):
        super().fun1()
        print("Method 4!!")
        
obj = Myclass4()
obj.fun1()