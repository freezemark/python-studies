count = eval(input("Сколько хотите пицц? "))
price = eval(input("Сколько стоит 1 пицца в ₽? "))
tax = 0.08
cost = count * price
tax_cost = cost * tax

print("\nОбщая стоимость всех пицц: ₽", cost + tax_cost)
print(" ... в том числе ₽", cost, " за пиццы")
print(" ... и ₽", tax_cost, " налог")

