# Problem 1
a=input("Enter the first Number: ")
a=int(a)
b=input("Enter the second Number: ")
b=int(b)
c=input("Enter he third Number: ")
c=int(c)
avg=((a+b+c)/3)
print(avg)

#Problem 2
gi=input("Enter the gross income: ")
gi=int(gi)
nod=input("Enter the number of dependents: ")
nod=int(nod)
sd=10000
a_d=3000
Taxable_Income=gi-sd-(nod*a_d)
Income_tax=Taxable_Income*20/100
if Income_tax<0:
    Income_tax=0
else: print("Taxable Income: $", Taxable_Income)
print("Income tax: $", Income_tax)

#Problem 3
s=int(input("Enter the number of seconds: "))
m=s//60
s1=s%60
print(m,"Minutes", s1,"Seconds")

#Problem 4
a=25
b="25"
c=25.0
d=(int(a)+int(b)+int(c))
print(str(d))

#Problem5
import math 
for x in range(0,346,15): print(x,'---',round(math.sin(x),4), round(math.cos(x),4))

