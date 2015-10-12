"""
I think this is based on the theory
(suppose b = 2^k)
a^b = ((((a^2)^2)...)^2)
a^(p1*p2*p3) = (((a^p1)^p2)^p3)

O(logb)
"""
def recurPowerNew(a, b):
   print a, b
   if b == 0:
      return 1
   elif b%2 == 0:
      return recurPowerNew(a*a, b/2)
   else:
      return a * recurPowerNew(a, b-1)
