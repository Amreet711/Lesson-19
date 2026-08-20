import random 
import math
lucky_number=random.randint(1,10)
print("Lucky Number: ",lucky_number)
fun_activities=["Draw a picture","Play a game","Solve a puzzle","Read a book","Learn a new skill"]
choice=random.choice(fun_activities)
print("Your fun activity is",choice)
secret_number=random.randint(1,5)
while True:
    guess=int(input("Can you guess the secret number? (Hint: It's between 1 and 5)"))
    if guess == secret_number:
        print("CORRECT")
        break
    else:
        print("INCORRECT")
decimal_number=float(input("Please enter a decimal number:"))
ceil=math.ceil(decimal_number)
floor=math.floor(decimal_number)
print(f"The ceil and floor values of {decimal_number} are {ceil} and {floor}")
x=int(input("Please enter a negative whole number:"))
y=int(input("Please enter a positive whole number:"))
print("If we copy the sign of the first number and add it to the second we get", math.copysign(x,y))
print("The absolute values of the two numbers are ", math.fabs(x)," and ", math.fabs(y))
print ("The Greatest Common Diviser of the two numbers is ",math.gcd(x,y))
print("====== Fun Calculator Summary ======")
print(f"LUCKY NUMBER:{lucky_number}")
print(f"ACTIVITY CHOICE:{choice}")
print(f"SECRET NUMBER:{secret_number}")
print(f"DECIMAL NUMBER:{decimal_number}")
print(f"CEIL VALUE:{ceil}")
print(f"FLOOR VALUE:{floor}")
print(f"NUMBER 1:{x}")
print(f"NUMBER 2:{y}")
print("COPYSIGN VALUE:", math.copysign(x,y))
print("ABSOLUTE VALUE (Number 1):",math.fabs(x))
print("ABSOLUTE VALUE (Number 2):",math.fabs(y))
print("GREATEST COMMON DIVISER:",math.gcd(x,y))
print("======================================")
