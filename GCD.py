def gcd(x,y):
    if x == 0:
        print(y,"is the gcd")
    elif y == 0:
         print(x,"is the gcd")
    else:
          div = x
          div1 = y
          while (1==1):
               remainder = div % div1
               if (remainder == 0):
                    return div1
               else:
                    div = div1
                    div1 = remainder




num1 = int(input("enter the numbers:"))
num2 = int(input("enter the numbers:"))
print (f"thr gcd of {num1} and {num2} is {gcd(num1,num2)}")
