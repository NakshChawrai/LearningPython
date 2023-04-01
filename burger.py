# atlantaburger.py
currency_symbol="₹"
number_of_burgers=eval(input("How many burgers do you want: "))
cost_per_burger=eval(input("How much does each burger cost:₹ "))
subtotal = number_of_burgers * cost_per_burger
tax_rate=0.08
sales_tax=subtotal * tax_rate
total= subtotal + sales_tax
print("The total cost is ", currency_symbol,total)
print("This includes ",currency_symbol,subtotal,"for the burger and")
print(currency_symbol,sales_tax,"in sales tax")
