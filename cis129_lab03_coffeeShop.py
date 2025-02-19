#assign variables for coffee and muffins
coffee_price = 5
muffin_price = 4
coffee_amount = int(input('Number of coffees bought?'))
muffin_amount = int(input('Number of muffins bought?'))
coffee_total = coffee_price * coffee_amount
muffin_total = muffin_price * muffin_amount
base_price = coffee_total + muffin_total
tax = 0.06 * base_price
total_price = tax + base_price
#variable text passages for ease of coding
intro = '******************************\nMy Coffee and Muffin Shop\n'
middle = '\n******************************\n\n******************************\nMy Coffee and Muffin Shop Receipt\n'
coffee_text = 'Coffee at $5 each: $'
muffin_text = 'Muffins at $4 each: $'
tax_text = '6% tax: $'
#finalize display text and receipt
print( intro, int(input('Number of coffees bought?')), int(input('Number of muffins bought?')), muffin_amount, middle, coffee_amount, coffee_text, '.00\n', muffin_amount, muffin_text, '.00\n', tax_text, tax, '\n----------\nTotal: $', total_price, '\n******************************')
