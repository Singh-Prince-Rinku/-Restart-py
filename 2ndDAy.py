# Operators in python
# 1. Addition
# 2. Substraction
# 3. Multiplication
# 4. Division /
# 5.Remainder %
# 6. Exponential ** means if 5 ** 2 that is square of 5

a=int(input("Enter your value")) #Taking input from the user as integer 
b=int(input("Enter your value")) #Taking input from the user as integer
c=input("Enter your operators:")  #Here we take opereators as integer because in python if we take input without any data type then python take input as string:
if c=="+":   #you can se if condition with operators as string:
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="%":
    print(a%b)
else:
    print("Wrong Operators")


name="Prince"
print(name[-4:-2])