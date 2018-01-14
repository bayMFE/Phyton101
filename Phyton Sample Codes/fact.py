import math

a= (math.factorial(10000)/(math.factorial(10000)*math.factorial(0)))
b= ((0.001)**0)*((1-0.001)**10000)
#print(a*b)

c= (math.factorial(10000)/(math.factorial(9999)*math.factorial(1)))
d= ((0.001)**1)*((1-0.001)**9991)
#print(a*b)

e= (math.factorial(10000)/(math.factorial(9998)*math.factorial(2)))
f= ((0.001)**2)*((1-0.001)**9998)
print((a*b)+(c*d)+(e*f))
