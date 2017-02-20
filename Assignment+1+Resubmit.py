
# coding: utf-8

# In[45]:

#Program 1

#What is your name
name = input("What is your name? ")

#greeting
greeting = "Hello " + name + " nice to meet you!"

print(greeting)


# In[49]:

#Program 2

#What is the input string
name = input("What is the input string? ")

lenofname = len(name)
print(name + ", has " +str(lenofname) + " charactors.")


# In[50]:

#Program 3
#Mad libs
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
output = "Do you " + verb + " your " + adjective + " " + noun + " " + adverb + "? That is hilarious!"
print(output)


# In[ ]:

#Program 4
first = int(input("What is the first number? "))
second = int(input("What is the second number? "))
summation = first + second
subtraction = first - second
product = first*second
division = first/second
print(summation)
print(subtraction)
print(product)
print(int(division))


# In[ ]:

#Program 5
age = input("What is your current age? ")
retireage = input("At what age would you like to retire? ")
yearsleft = int(retireage) % int(age)
import datetime
now = datetime.datetime.now()
retire = "It's " + str(now.year) + " , so you can retire in "+ (str(now.year+yearsleft)) + "."
print(retire)


# In[ ]:

first - second
product = first*second
division = first/second
print(summation)
print(subtraction)
print(product)
print(int(division))


# In[ ]:




# In[4]:

#Program 6 Area Calculation
length = int(input("What is the length of the room in feet? "))
width = int(input("What is the width of the room  in feet? "))
area = length*width
squaremeters = area*0.09290304
print(area)
print(round(squaremeters,3))


# #Program 7 Pizza Divide
# people = input("How many people? ")
# pizza = input("How many pizzas do you have? ")
# slices = input("How many slices per pizza? ")
# peoplepizza = people+" people with "+pizza+" pizza"
# print(peoplepizza)
# eachperson = "Each person gets "+pizza+" pieces of pizza."
# print(eachperson)
# print("There are 0 leftover pieces.")

# In[9]:

#Program 7 Pizza Divide
people = int(input("How many people? "))
pizza = int(input("How many pizzas do you have? "))
slices = int(input("How many slices per pizza? "))
peoplepizza = str(people)+" people with "+str(pizza)+" pizza"
print(peoplepizza)
eachperson = "Each person gets "+str(int(people*pizza/slices))+" pieces of pizza."
print(eachperson)
print("There are 0 leftover pieces.")


# In[23]:

#Problem 8 Paint
area = int(input("How many square feet do you have? "))
gallon = 350
need=round(int(area/gallon),0)+1
print("You will need to purchase " + str(need)+" gallons to cover "+str(area) +" square feet.")


# #Program 9 Self-checkout system
# price1 = input("Enter the price of item 1: ")
# quantity1 = input("Enter the quantity of item 1: ")
# price2 = input("Enter the price of item 2: ")
# quantity2 = input("Enter the quantity of item 2 ")
# price3= input("Enter the price of item 3")
# quantity3 = input("Enter the quantity of item 3 ")
# Subtotal = price1*quantity1+price2*quantity2+price3*quantity3
# print(Subtotal)
# Tax=Subtotal*0.055
# print(Tax)
# Total=Subtotal+Tax
# print(Total)

# In[37]:

#Program 9 Self-checkout system
price1 = int(input("Enter the price of item 1: "))
quantity1 = int(input("Enter the quantity of item 1: "))
price2 = int(input("Enter the price of item 2: "))
quantity2 = int(input("Enter the quantity of item 2 "))
price3= int(input("Enter the price of item 3"))
quantity3 = int(input("Enter the quantity of item 3 "))
subtotal = price1*quantity1+price2*quantity2+price3*quantity3
print("Subtotal: $"+str(subtotal))
tax=subtotal*0.055
print("Tax: $"+str(tax))
total=subtotal+tax
print("Total: $"+str(total))


# In[40]:

#Program 10 Interest Calculation
principal = float(input("Enter the principal: "))
rateofinterest = float(input("Enter the rate of interest: "))
years = int(input("Enter the number of years: "))
A=principal*(1+rateofinterest/100*years)
investment = "After "+str(years)+" years at "+str(rateofinterest)+"%, the investment will be worth $"+str(A)
print(investment)


# In[ ]:



