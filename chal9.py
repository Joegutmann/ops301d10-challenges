# Joe Gutmann
# 12.7.23
# Python Conditional Statements

#Equals: a == b
a = 100
b = 125

if a == b:
    print("You have reached break even")
else:
    print("You may be losing money after fees")

#Not Equals: a != b

a = 100
b = 155

if a != b:
    print("maybe lose money, maybe you net some. Know your costs")
else: 
    print("you are definitely losing money")
#Less than: a < b

a = 100
b = 125

if a < b:
    print ("hopefully you will net some")
else:
    print("I'm sorry")
#Less than or equal to: a <= b

a = 100
b = 125

if a <= b:
    print("congrats, you are definitely making money this time!")
else:
    print("most likely you are losing money")
#Greater than: a > b

a = 100
b = 125

if a > b:
    print("your'e losing money again/ Welcome to the trading card world")
else:
    print("Small to large profit margins are found here")
#Greater than or equal to: a >= b

a = 100
b = 125

if a >= b:
    print("100% money is lost.")
else:
    print("again, neglible to potentially significant gains")
#Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

a = 5
b = 25

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")

#Create an if statement that includes both elif and else to execute when both if and elif are not met.
age = 21

if age < 21:
    print("no drinkey for you")
elif age >= 21:
    print("yes you may drink here")
else:
    print("how old are you?")

