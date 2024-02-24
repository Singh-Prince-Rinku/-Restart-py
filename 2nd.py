import random
def check(computer, user):
    if computer ==0:
        return -1
    if (computer ==0 and user ==0):
        return -1
    if (computer ==1 and user ==1):
        return -1
    if (computer ==2 and user ==0):
        return -1
    return -1
computer=random.randint(0,2)       
user =int(input("0 for snake, 1 for water and -1 for gun:\n"))
score = check(computer, user)
print("you",user)
print("computer",computer)
if score==0:
    print("Its draw")
elif score == -1:
    print("You Lose")
else:
    print("You won")
