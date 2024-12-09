#First python function

#def is the keyword used to define function
#This is called function declaration

def nameofthefunction(sentence):
    print(sentence)
#calling a function

nameofthefunction("this_is_first_function")

def adding_twonumbers(a,b):
    c=a+b
    print(c)
adding_twonumbers(5,6)


def multiplytwonumbers():
    a=5
    b=10
    c=a+b
    print(c)
multiplytwonumbers()

#return statement

def getaadharnumber():
    return "123 456 789"
print(getaadharnumber())


#1:apple
#2:orange
#3:mango
#4:banana


def calling_fruits(num):
    fruit_name=""
    if num==1:
        fruit_name="apple"
    elif num==2:
        fruit="orange"
    elif num==3:
        fruit="mango"
    elif num==4:
        fruit="banana"
    else:
        fruit_name="no fruit"
    return fruit_name
print(calling_fruits(2))

#pass string and return integer



calling_fruits(3)


