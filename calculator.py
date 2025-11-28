import math
num1= input("enter first number: ")
operator= input ("Enter the operation (+,-,*,/,clear)")
num2=input("Enter the second number:")

num1=float(num1)
num2=float(num2)

if operator=='+':
    result=num1+num2
elif operator=='-':
    result=num1=num2
elif operator=='*':
    result =num1*num2
elif operator=='/':
    if num2 !=0:
        result=num1/num2
    else:
        result="error:division by zero"
elif operator=='clear':
    result=0
else:
    result="error:invalid operator"
print(num1,operator,num2,"=",result)
    
    
        
