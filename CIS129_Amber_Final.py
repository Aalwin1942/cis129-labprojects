from AZTaxLibrary import AZ_Taxes
def Welcome():
    print('Welcome to TransparaTAX!\nAn Arizona sales tax calculator!\nCalculate individual prices or create a shopping cart!\nSee the price before you checkout!')
    print('This calculator has a database of city and county taxes in Arizona sourced from tax-rates.org')
    see_list = input('To see a list of cities and counties in our database type "Yes", to continue to the program type "No": ')
    see_list = see_list.upper()
    while see_list not in ['YES', 'NO']:
        print('Entry invalid.')
        see_list = input('Please type "Yes" to see the list, or "No" to continue: ')
        see_list = see_list.upper()
    if see_list == 'YES':
        for place in AZ_Taxes.keys():
            print(place, end=', ')
    else:
        print('\n')
def LocationInput():
    print('For this program city has priority over county, so if both are applicable enter the city.')
    location = input('Enter city or county: ')
    while location.upper() not in AZ_Taxes.keys():
        print('This submission is not in our database. Please check spelling and try again.')
        location = input('Enter city or county: ')
    global sales_tax
    sales_tax = float(AZ_Taxes[location.upper()])
    print(f'Sales tax for {location} is {sales_tax}')
    return sales_tax
def IndividualCalc():
    calc_tax = sales_tax / 100
    item = float(input('Enter cost of item (excluding dollar sign): '))
    amount = int(input('Enter unit amounts: '))
    global cost
    cost = ((item * calc_tax) + item) * amount
    print(f'The price after tax is: {cost:.2f}. Unit price is {(item * calc_tax) + item:.2f}')
    return cost
def Cart():
    global add_item
    add_item = input('Add item to cart? (Enter "Yes" or "No"): ')
    add_item = add_item.upper()
    while add_item not in ['YES', 'NO']:
        print('Entry Invalid. Try again.')
        add_item = input('Add item to cart? (Enter "Yes" or "No"): ')
        add_item = add_item.upper()
    if add_item == 'YES':
        global cart
        cart += cost
        print(f'Cart total: {cart:.2f}')
    return cart, add_item
def cartloop():
    endloop = input('To exit type "E", to add more items type "C": ')
    while endloop not in ['E', 'e']:
        IndividualCalc()
        Cart()
        endloop = input('To exit type "E", to add more items type "C": ')
        endloop.upper()
    return endloop
def restart():
    global again
    again = input('To continue with a cart type "Cart".\nTo perform an individual calculation type "Solo".\nTo exit the program type "Done": ')
    while again.upper() not in ['CART', 'SOLO', 'DONE']:
        print('Input invalid, try again.')
        again = input('To continue with a cart type "Cart".\nTo perform an individual calculation type "Solo".\nTo exit the program type "Done": ')
        again.upper()
    while again.upper() in ['CART', 'SOLO']:
        if again.upper() == 'CART':
            IndividualCalc()
            Cart()
            cartloop()
        elif again.upper() == 'SOLO':
            print('Solo item mode!')
            IndividualCalc()
            endSolo = input('To end type "E", to continue type "C": ')
            if endSolo.upper() == 'E':
                again = 'EXIT'
    return print('Thank you for using TransparaTAX! Have a great day!')
endloop = 0   
again = 0            
cart = 0
add_item = 0
Welcome()
LocationInput()
IndividualCalc()
Cart()
if add_item.upper() == 'YES':
    while add_item.upper() == 'YES' and again not in ['DONE', 'done']:
        cartloop()
        if endloop == 'C':
            IndividualCalc()
            Cart()
        else:
            restart()
else:
    restart()
