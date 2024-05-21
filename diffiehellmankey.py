
def root(p, g):
    powers = {}
    for i in range(1, p):
        result = (g,i,p)
        powers[result] = i
    return powers

def diffie_hellman(p, g, a, b):
    powers = root(p, g)
    A = pow(g,a,p)
    B = pow(g,b,p)
    k1 = pow(B,a,p)
    k2 = pow(A,b,p)
    return k1, k2

p = int(input("Enter the prime modulus (p): "))
g = int(input("Enter the generator (g): "))
a = int(input("Enter Alice's private key (a): "))
b = int(input("Enter Bob's private key (b): "))

kA, kB = diffie_hellman(p, g, a, b)

print("Shared Key of Alice:", kA)
print("Shared Key Bob:", kB)

if kA == kB:
  print("Shared keys match.")
else:
  print("Shared keys do not match.")