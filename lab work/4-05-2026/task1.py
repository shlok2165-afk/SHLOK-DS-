try:
    n=int(input("Enter Number : "))

    if n % 2== 0:
        print("Even")
        
    else :
        print("Odd")
        
except  ValueError as e:
    print(e)
    
else:
    print("Try Excucated ")
    
finally:
    print("finally Excucated")