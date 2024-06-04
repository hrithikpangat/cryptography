from primeornot import isPrime
from prime_factors import primeFactors

def calculate_G(P):
    eulerstotient = P-1
    factors = list((primeFactors(eulerstotient)))
    for j in range (2,P):
        for i in factors:
            calcuate1 = eulerstotient // i
            calcuate2 = pow(j,calcuate1)
            G = calcuate2 % P 
            if G == 1:
                break
            else:
                return j
            

if __name__ == "__main__":
    P = int(input("Enter the prime number(p):"))
    Genrator = calculate_G(P)
    checkprime = isPrime(P)
    if checkprime == 1:
        print(f"Generator --->{Genrator}")

        privatekey1 = int(input("Enter the private key for user-1:"))
        privatekey2 = int(input("Enter the private key for user-2:"))
       
        publickey1 = pow(Genrator,privatekey1,P)
        publickey2 = pow(Genrator,privatekey2,P)

        symmetrickey1 = pow(publickey1,privatekey2,P)
        symmetrickey2 = pow(publickey2,privatekey1,P)

        print(f"The symmetric key for user 1 :{symmetrickey1}")
        print(f"The symmetric key for user 2 :{symmetrickey2}")

    else:
        print("Enter a prime number")

    

