myAge = 32
yourAge = 18
myNumber = 81
yourNumber = 17
votingAge = 18
if myAge == 31 and yourAge < myAge:
  print('My age is 31 and your age is less than that')
if myAge <= 35 and myAge >= 32:
  print('My age is between 32 and 35')
if yourAge == votingAge or yourAge > votingAge:
  print('You can vote')
if myNumber == 83 or yourNumber == 83:
  print('One of our numbers is 83')
if myAge == 31 and yourAge < myAge:
  print('My age is 31 and your age is less than that')
else:
  print('Our ages do not qualify')
if myAge <= 35 and myAge >= 32:
  print('My age is between 32 and 35')
else:
  print('My age is not within that range')
if yourAge == votingAge or yourAge > votingAge:
  print('You can vote')
else:
  print('You cannot vote')
if myNumber == 83 or yourNumber == 83:
  print('One of our numbers is 83')
else:
  print('83 is not out numbers')


# Module 4 Lab-4
#Amber
#25 Feb 2025
#Program provides store bonus based off of monthly sales and employee bonus based on monthly sales percentage increase
#declare local variables
monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease = 0 # percent of sales increase
prompt = 'Enter monthly sales amount:' # prompt will be a string literal
# this code gets the monthly sales
monthlySales = float(input(prompt))
# this code determines the store bonus
if monthlySales >= 110000:
  storeAmount = 6000
elif monthlySales >= 100000:
  storeAmount = 5000
elif monthlySales >= 90000:
  storeAmount = 4000
elif monthlySales >= 80000:
  storeAmount = 3000
else:
  storeAmount = 0
# this code gets the percent of increase in sales
salesIncrease = float(input('Enter sales increase percentage:'))
# this code determines the employee bonus
salesIncrease = salesIncrease / 100
if salesIncrease >= 0.05:
  empAmount = 75
elif salesIncrease >= 0.04:
  empAmount = 50
elif salesIncrease >= 0.03:
  empAmount = 40
else:
  empAmount = 0
# this code prints the bonus information
print('The store bonus amount is $', storeAmount)
print('The employee bonus amount is $', empAmount)
if (storeAmount == 6000) and (empAmount == 75):
  print('Congrats! You have reached the highest bonus amounts possible!')

