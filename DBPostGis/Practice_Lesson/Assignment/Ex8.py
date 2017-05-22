import cmath,math
print 'Solve the quadratic equation'
a=float(raw_input('Enter Coeffients a: '))
b=float(raw_input('Enter Coeffients b: '))
c=float(raw_input('Enter Coeffients c: '))

delta= b*b - 4*a*c
if delta>0:
    x1=-b-math.sqrt(delta)/2*a
    x2=-b+math.sqrt(delta)/2*a
elif delta==0:
    x1=x2=-b/2*a
else:
    x1 = -b - cmath.sqrt(delta) / 2 * a
    x2=x2=-b+cmath.sqrt(delta)/2*a
print 'X1: ' +str(x1)
print 'X2: '+str(x2)
