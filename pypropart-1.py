#  1.Program to Print Hello world!
# print("Hello world!")

# 2.Program to Add Two Numbers
'''a = int(input("enter first number:"))
b = int(input("enter second number:"))
sum = a+b
print(sum)'''

# 3.Program to Find the Square Root
# 1 method
'''import math
a = int(input("enter a number:"))
print(int(math.sqrt(a)))'''

#2nd method
'''num = int(input("enter a number:")) 

num_sqrt = num ** 0.5
print('the square root of %0.3f is %0.3f'%(num ,num_sqrt))'''

#4.program to find the area of a traingle 
'''b = int(input('enter breadth:'))
h = int(input('enter a height:'))

ar_of_tra = 1/2 *b*h 
print("area of a traingle",ar_of_tra)'''

#5.program to solve quadratic equation
'''import cmath

a = int(input("enter a :"))
b = int(input("enter b :"))
c = int(input("enter c :"))

d = (b**2) -(4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("the solution are {0} and {1}".format(sol1,sol2))'''

#6.program to swap 2 numbers
'''x = int(input("enter value x:"))
y = int(input("enter value y:"))

temp = x 
x = y
y = temp

print("the value of x after swapping :{}".format(x))
print("the value of y after swapping :{}".format(y))'''

#or

'''x = int(input("enter value x:"))
y = int(input("enter value y:"))

x,y = y,x

print("x =",x)
print("y =",y)'''

#if the variables are both numbers 
#Here are a few examples:
# addition & sub
'''x = x + y
y = x - y
x = x - y'''
#div & mul 
'''x = x * y  
y = x / y    
x = x / y''' 

#7.python program to generate a random number:
'''import random

print(random.randint(0,9))'''

#8.program to convert kilometeres to miles 
'''kilometres = float(input("enter value in kilometeres:"))
 
#conversion factor 
conv_fac = 0.621371

#calculate miles
miles  =  kilometres * conv_fac 
print("%0.2f kilometers is equal to %0.2f miles" %(kilometres,miles))'''

#9.program to convert Celsius to Farenheit
#fahrenheit = (celsius * 1.8) + 32
#convert celsius to Farenheit 
'''celsius = float(input('enter a celsius number:'))

# celsius to farhenheit
Farenheit = (celsius * 1.8) + 32
print("%0.1f to degree celsius is equal to %0.1f degree Farenheit"%(celsius,Farenheit))

#farenheit to celsius
Farenheit = float(input('enter a Farenheit number:'))
celsius = (Farenheit -32)/1.8

print("%0.1f to degree celsius is equal to %0.1f degree Farenheit"%(Farenheit,celsius))'''

#python program to check if a number is +ve or -ve or zero 
#1.if..elif..else
'''num = int(input("enter a number:"))

if num>0:
    print("the number is positive")
elif num==0:
    print("zero")
else:
    print("negative number")'''

#2.nested if else
'''num = int(input("enter a number:"))

if num >=0:
    if num == 0:
        print("zero")
    else:
        print("postive number")
else:
    print("Negative number")'''




