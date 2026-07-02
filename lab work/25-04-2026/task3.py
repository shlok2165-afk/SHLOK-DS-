# class Myclass:
    
#     def fun1(self):
#         print("Method 1!!")
        

# class Myclass1(Myclass):
    
#     def fun2(self):
#         print("Method 2!!")
        

# obj = Myclass1()
# obj.fun1()
# obj.fun2()




class Myclass:
    
    def fun1(self):
        print("Method 1!!")
        

class Myclass1:
    
    def fun2(self):
        print("Method 2!!")
   
   
class Myclass2(Myclass,Myclass1):
    
    def fun3(self):
        print("Method 3!!")     

 
obj = Myclass2()
obj.fun1()
obj.fun2()
obj.fun3()