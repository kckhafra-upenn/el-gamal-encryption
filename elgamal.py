import random
from math import pow

from params import p
from params import g
q=(p-1)/2
def power(A, B, C):
     
    # Base Cases
    if (A == 0):
        return 0
    if (B == 0):
        return 1
     
    # If B is Even
    y = 0
    if (B % 2 == 0):
        y = exponentMod(A, B / 2, C)
        y = (y * y) % C
     
    # If B is Odd
    else:
        y = A % C
        y = (y * exponentMod(A, B - 1,
                             C) % C) % C
    return ((y + C) % C)

def keygen():
    sk = 0
    pk = 0
    
    sk = random.randint(1, q)
    pk = power(g,sk,p)
    return pk,sk

def encrypt(pk,m):
    c1 = 0
    c2 = 0
    
    # r= random.randint(1, q)
    r=random.randint(1, q)
    c1= power(g,r,p)
    # hr⋅m mod p in your code: (ab) mod c = ((a mod c) * (b mod c)) mod c
    # pk^r*m mod p
    c2= (power(pk,r,p)*(m%p))%p
    return [c1,c2]
    
def decrypt(sk,c):
    m = 0
    e = p-sk-1
    m=(power(c[0],e,p)*(c[1]%p))% p
    # h^r⋅m mod p in your code: (ab) mod c = ((a mod c) * (b mod c)) mod c
    # pk^r*m mod p
    return m