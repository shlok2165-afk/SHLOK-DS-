# polymorpism   poly - Many

# morphism - forms 

#  2 method : 
     
     
# 1) method overloading : same name of method in single class - not supported in python 

# 2) method overriding : same name with ingerited class 


class A :
    def fun1(self):
        print("Method 1 ")
        
        
class B(A):
    def fun1(self):
        super().fun1()
        print("method 2 ")
       
    
    
obj =B()
obj.fun1()