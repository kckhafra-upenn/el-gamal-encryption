import random
from math import pow

from params import p
from params import g
# q=(p-1)/2
def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c

# def gcd(a, b):
#     if a < b:
#         return gcd(b, a)
#     elif a % b == 0:
#         return b
#     else:
#         return gcd(b, a % b)

def keygen():
    sk = 0
    pk = 0
    
    sk = random.randint(1, p)
    pk = power(g,sk,p)
    # print(sk)
    # print(pk)
    return pk,sk

def encrypt(pk,m):
    c1 = 0
    c2 = 0
    
    # r= random.randint(1, q)
    r=random.randint(1, p)
    c1= power(g,r,p)
    # hr⋅m mod p in your code: (ab) mod c = ((a mod c) * (b mod c)) mod c
    # pk^r*m mod p
    c2= (power(pk,r,p)*(m%p))%p
    return [c1,c2]
    
def decrypt(sk,c):
    m = 0
    e = p-sk-1
    m=(power(c[1],e,p)*(c[2]%p))% p
    # h^r⋅m mod p in your code: (ab) mod c = ((a mod c) * (b mod c)) mod c
    # pk^r*m mod p
    return m

# keygen()
# a,b = 5,7
# x = pow(a,-1,b)
# assert x*a % b == 1
# print(x)