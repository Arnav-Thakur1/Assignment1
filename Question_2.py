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