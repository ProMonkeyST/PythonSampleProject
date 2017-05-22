print 'Calculator'
num1=float(raw_input('Enter First Number: '))
num2=float(raw_input('Enter Second Number: '))
operation=(raw_input('Enter operation(+,-,*,/): '))

if operation=='+':
    result=num1+num2
elif operation=='-':
    result=num1-num2
elif operation=='*':
    result=num1*num2
elif operation=='/':
    result=num1/num2
else:
    print 'Error! Invalid Input'
print 'Result: '+str(result)