#assign variables for coffee and muffins
coffee_price = 5
muffin_price = 4
bagel_price = 6
tea_price = 3
coffee_amount = int(input('Number of coffees bought?'))
muffin_amount = int(input('Number of muffins bought?'))
bagel_amount = int(input('Number of bagels bougt?'))
tea_amount = int(input('Number of teas bought?'))
coffee_total = coffee_price * coffee_amount
muffin_total = muffin_price * muffin_amount
bagel_total = bagel_price * bagel_amount
tea_total = tea_price * tea_amount
base_price = coffee_total + muffin_total + bagel_total + tea_total
tax = 0.06 * base_price
total_price = tax + base_price
#variable text passages for ease of coding
intro = '******************************\nMy Coffee and Muffin Shop\n'
middle = '\n******************************\n\n******************************\nMy Coffee and Muffin Shop Receipt\n'
coffee_text = 'Coffee at $5 each: $'
muffin_text = 'Muffins at $4 each: $'
bagel_text = 'Bagels at $6 each: $'
tea_text = 'Tea at $3 eac: $'
tax_text = '6% tax: $'
#finalize display text and receipt
print( intro, int(input('Number of coffees bought?')), int(input('Number of muffins bought?')), int(input('Number of bagels bougt?')), int(input('Number of teas bought?')), middle, coffee_amount, coffee_text, '.00\n', muffin_amount, muffin_text, '.00\n', bagel_amount, bagel_text, '.00\n', tea_amount, tea_text, '.00\n', tax_text, tax, '\n----------\nTotal: $', total_price, '\n******************************')
#updates adding bagel and tea
