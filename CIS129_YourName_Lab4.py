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


# include code to get the monthly Sales
# include code to get the Increase in Sales
# include code to Calculate the Store Bonus
# include code to Calculate the Employee Bonus
# include code to print out all the results

monthlySales = float(input('Enter monthly sales amount:'))
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
salesIncrease = float(input('Enter sales increase percentage:'))
salesIncrease = salesIncrease / 100
if salesIncrease >= 0.05:
  empAmount = 75
elif salesIncrease >= 0.04:
  empAmount = 50
elif salesIncrease >= 0.03:
  empAmount = 40
else:
  empAmount = 0
print('The store bonus amount is $', storeAmount)
print('The employee bonus amount is $', empAmount)
if (storeAmount == 6000) and (empAmount == 75):
  print('Congrats! You have reached the highest bonus amounts possible!')

