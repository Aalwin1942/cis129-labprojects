#text sortcuts
coffee_q = 'Number of coffees bought?'
muffin_q = 'Number of muffins bought?'
bagel_q = 'Number of bagels bought?'
tea_q = 'Number of teas bought?'
#assign variables for coffee and muffins
coffee_price = 5
muffin_price = 4
bagel_price = 6
tea_price = 3
coffee_amount = int(input(coffee_q))
muffin_amount = int(input(muffin_q))
bagel_amount = int(input(bagel_q))
tea_amount = int(input(tea_q))
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
tea_text = 'Tea at $3 each: $'
tax_text = '6% tax: $'
#finalize display text and receipt
print( intro, coffee_q, '\n', coffee_amount, '\n' , muffin_q , '\n', muffin_amount, '\n', bagel_q, '\n', bagel_amount, '\n', tea_q, '\n', tea_amount, '\n', middle, coffee_amount, coffee_text, coffee_total, '.00\n', muffin_amount, muffin_text, muffin_total, '.00\n', bagel_amount, bagel_text, bagel_total, '.00\n', tea_amount, tea_text, tea_total, '.00\n', tax_text, tax, '\n----------\nTotal: $', total_price, '\n******************************')
#updates adding bagel and tea
