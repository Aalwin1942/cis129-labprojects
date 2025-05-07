import AZTaxLibrary.py
def Welcome():
    print('Welcome to our Arizona sales tax calculator!\nCalculate individual prices or create a shopping cart!\nSee the price before you checkout!')
    print('This calculator has a database of city and county taxes in Arizona sourced from tax-rates.org')
    see_list = input('To see a list of cities and counties in our database type "Yes", to continue to the program type "No": ')
    see_list = see_list.upper()
    while see_list not in ['YES', 'NO']:
        print('Entry invalid.')
        see_list = input('Please type "Yes" to see the list, or "No" to continue: ')
        see_list = see_list.upper()
    if see_list == 'YES':
        for place in AZ_Taxes.key():
            print(place, end=', ')
    else:
        print('\n')
sales_tax = 0
def LocationInput():
    print('For this program city has priority over county, so if both are applicable enter the city.')
    location = input('Enter city or county: ')
    while location.upper() not in AZ_Taxes.key():
        print('This submission is not in our database. Please check spelling and try again.')
        location = input('Enter city or county: ')
    sales_tax = AZ_Taxes[location.upper()]
    return sales_tax
cost = 0
def IndividualCalc():
    item = float(input('Enter cost of item (excluding dollar sign): '))
    amount = int(input('Enter unit amounts: '))
    cost = item * amount * sales_tax
    print(f'The price after tax is: {cost}. Unit price is {item * sales_tax}')
    return cost
cart = 0
def Cart():
    add_item = input('Add item to cart? (Enter "Yes" or "No"): ')
    add_item = add_item.upper()
    while add_item not in ['YES', 'NO']:
        print('Entry Invalid. Try again.')
        add_item = input('Add item to cart? (Enter "Yes" or "No"): ')
        add_item = add_item.upper()
    if add_item == 'YES':
        cart += cost
Welcome()
LocationInput()
print(sales_tax)
