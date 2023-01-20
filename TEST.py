
plus_or_times = input("+ or x or : or -? =  ")

num1 = input("enter any number and press enter: ")
num2 = input("enter another number and press enter: ")

if plus_or_times == 'x': ans = float(num1) * float(num2)
if plus_or_times == '+': anwser: int = float(num1) + float(num2)
if plus_or_times == ':': answ: int = float(num1) // float(num2)
if plus_or_times == '-': ans1: int = float(num1) - float(num2)
if plus_or_times == ':': print(answ)
if plus_or_times == '+': print(anwser)
if plus_or_times == 'x': print(ans)
if plus_or_times == '-': print(ans1)
