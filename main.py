#!/usr/bin/python

import random
import sys
from time import time



def gcd( a, b ):
		while b != 0:
			c = a % b
			a = b
			b = c
		#a is returned if b == 0
		return a


def pow(x, y):
    """Raise x to the power y, where y must be a nonnegative integer."""
    result = 1
    for _ in range(y):   # using _ to indicate throwaway iteration variable
        result *= x
    return result



# Python Program to find the L.C.M. of two input number

# define a function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm



t1 = time()
try:
    p=int(input('p:'))
    q=int(input('q:'))
    r=int(input('r:'))
except ValueError:
    print ("Not a number")


p_1 = p-1
q_1 = q-1
n = p*q
pq = (p_1) * (q_1)
if (p == q):
    print ("Given values are same. Enter another values")
else:
    if (gcd(n, pq) == 1):
        lamb = lcm(p_1, q_1)
        print ( "gcd is :", lamb)
        g = r *n
        print("g=",g)
    else:
        print ("select other values.")

#encryption

m= int(input('m:'))

x = pow(g,m)
y= pow(r,n)
z= x*y
n2= n**2
print(z)
print("n square value is:", n2)
cipher = divmod(z,n2)
w= cipher[0]
print ("cipher test is:",w)
size = w.bit_length()
size2 = m.bit_length()
print ("message size is:", size2)
print("size of cipher text is:", size)
t2 = time()
print ("Encryption time is:",t2 - t1)
