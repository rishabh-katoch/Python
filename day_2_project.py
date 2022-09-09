#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = int(input("Enter the bill amount: "))
people =  int(input("How many people will split the bill: "))
tip = int(input("Tip in %age to be given: "))

amount = round((bill/people)*(1+(tip/100)),2)
print(f"The total amount to be paid per person is {amount}")