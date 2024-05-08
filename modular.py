from GCD import gcd
def modular_addition(x,y,z):
    addition = (x + y) % z
    return addition

def modular_multipilcation(x,y,z):
    multiplication = (x * y) % z 
    return multiplication

def modular_inverse(a,b):
    inverse = gcd(a,b) 
    if inverse == 1:
        c = 0
        while(True):
            multi = modular_multipilcation(a,c,b)
            if multi  == 1:
                return c
            c = c+1 
                
if __name__ == '__main__':

    x = int(input("ENTER THE NUMBER:"))
    y = int(input("ENTER THE SECOND NUMBER:"))
    z = int(input("ENTER THE DIVISOR:"))
    q = str(input("ENTER THE OPERATION:"))

    if q == "+":
        print(f"The modular addition of {x} and {y} is {modular_addition(x,y,z)}")
    elif q == "*":
        print(f"The modular multipilaction of {x} and {y} is {modular_multipilcation(x,y,z)}")
    else:
        print(False)

    a = int(input("ENTER THE NUMBER:"))
    b = int(input("ENTER THE NUMBER:"))
    print(modular_inverse(a,b))