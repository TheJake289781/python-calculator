
num1 = input("enter a number = ") # allows you to enter a number(need to press enter)
sign = input("enter: +, x, : = ") # allows you  to enter a sign pretty obvious
num2 = input("enter another number = ") # the same as the first line said

if sign == '+': # if + is pressed then add your numbers to eachother
    print(float(num1) + float(num2)) # the + = plus, num1(first numbers)  plus num2(second numbers)

if sign == 'x': # if x is pressed then multiply your numbers
    print(float(num1) * float(num2)) # the * = multiply, multiplies num1 with num2

if sign == ':': # if : is pressed then divide your numbers
    print(float(num1) / float(num2)) # the slash = divide, divides  
