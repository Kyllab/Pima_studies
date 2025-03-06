Lab4.py
"""""
script:  Module 4:Lab
action:  This program will breakdown the bonus structure of store
author:  Ackylla Burke
date:    03/05/25 """

def main():
 # declare local variables
   monthlySales = # monthly sales amount
   storeAmount= # store bonus amount
   empAmount= # employee bonus amount
   salesincrease= # percent of sales increase
 # call to getSales("enter monhtly sales amount" )
 # call to getIncrease("enter percent of increase in monthly sales")
 # call to calcStoreBonus(monthlySales )
 # call to calcEmpBonus(salesIncrease )
 # call to printBonus(storeAmount, empAmount)
 # This function gets the monthly sales

def getSales(prompt):
    monthlySales = float(input(prompt))
return monthlySales

# This function determines the storeAmount bonus
def calcStoreBonus(monthlySales):
if monthlySales >= 110000:
    storeAmount = 6000
elif if monthlySales >=100000:
    storeAmount = 5000
elif if monthlySales >=90000:  
    storeAmount = 4000
elif if monthlySales >=80000:
    storeAmount = 3000 
else if monthlySales <=79000:
return
    storeAmount=0

# This function gets the percent of increase in sales
 def getIncrease(prompt):
     salesIncrease = float(input(promt))
     salesIncrease = salesIncrease / 100
  return 
     storeAmount=5000 salesIncrease 0
# This function determines the empAmount bonus
 def calcEmpBonus(empAmount):
if   salesIncrease >= .05:
     empAmount = 75.00
elif salesIncrease >= .04:
     empAmount = 50.00
elif salesIncrease >= .03 :
     empAmount = 40.00
else: 
     empAmount = 0
return
    empAmount 0

# This function prints the bonus information
def printBonus(storeAmount,empAmount):
 print("The store bonus amount is $"6000)
 print("The employee bonus amount is $"75, )
 if ( == 6000 ) (empAmount ==550):
 print("Congrats! You have reached the highest bonus amounts
possible!")  

#calls main
main ()
