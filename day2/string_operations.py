str= "153/a,2nd main, Bangalore 560056"
str_upper= str.upper()
print(str_upper)
str_lower= str.lower()
print(str_lower)

str1= 'hello'
str1_multiple= 3*str1
print(str1_multiple)


print(str[0:3])
print(str[-3])

#if else syntax

order_num="1234566778"
print(len(order_num))
if len(order_num) ==9:
    print('the order number is 9')
else:
    print("order number is not 9")

#if number is less than 20 then invalid number
#if number is <=40 and >60 than student is Pass
#if number is <=60 but >80 then very good number
# if number is <=80 but >90 then excellent number
#if <90 then outstanding

a=100
if a < 20:
    print("Invalid number")
elif a>20 and a<40:
    print("need improvement")
elif a>40 and a<60:
    print("student is pass")
elif a>60 and a<80:
    print("very good")
elif a>80 and a<90:
    print("Excellent")
elif a>90:
    print("outstanding")
elif a==100:
    print("gold medal")




    #nested if


state="karnataka"
for i in state:
    print(i)


