# atlantapizza.py
currency_symbol="₹"
number_of_pizzas=eval(input("How many pizzas do you want: "))
cost_per_pizza=eval(input("How much does each pizza cost:₹ "))
subtotal = number_of_pizzas * cost_per_pizza
tax_rate=0.08
sales_tax=subtotal * tax_rate
total= subtotal + sales_tax
print("The total cost is ", currency_symbol,total)
print("This includes ",currency_symbol,subtotal,"for the pizza and")
print(currency_symbol,sales_tax,"in sales tax")
