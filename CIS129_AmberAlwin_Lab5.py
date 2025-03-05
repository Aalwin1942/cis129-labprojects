#name: Amber
#date: March 4, 2025
#program intended to calculate total bottle returns and subsequent payout for daily bottle inputs over period of a week

#Lab 5 The Bottle Return Program

#Step 1: declare variables below
today_bottles = 0 #number of bottles returned for the day
total_bottles = 0 #total bottles returned for the week
total_payout = 0  #totalBottles times .10cents per bottle
counter = 1 #accumulation variable to represent days of the week
keep_going = 'y' #loop stop/start variable

#Step 2: loop to run program again
while keep_going == 'y':
    total_bottles = 0
    for counter in range(1, 8):
        today_bottles = int(input(f'Enter number of bottles for day #{counter}:'))
    #Step 3: code to set value of variables
    #code to set value of variable total_bottles
        total_bottles += today_bottles
    #code to set value of variable total_payout
        total_payout = total_bottles * .10
    #code to print the number of total bottles and total payout
    print(f'The total number of bottles collected is {total_bottles}\nThe total paid out is ${total_payout:.2f}')
    print("Do you want to enter another week's worth of data?")
    keep_going = input('Enter (y or n):')
