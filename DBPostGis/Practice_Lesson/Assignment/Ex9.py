import math
print 'the area of triangle'

a=float(raw_input('Enter a: '))
b=float(raw_input('Enter b: '))
c=float(raw_input('Enter c: '))
p=(a+b+c)/2
area= math.sqrt(p*(p-a)*(p-b)*(p-c))

print 'Triangle Area: %d' %area
