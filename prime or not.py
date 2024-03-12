from math import sqrt
def is_prime(num):
    if num == 1:
        print("The number is niether prime nor composite")
    x = int(sqrt(num))+ 1
    for i in range(2,x):
        if (num % i == 0):
            return False
    return True

number = int(input("enter the number:"))
print(is_prime(number))




    
        
        
        
        
            

