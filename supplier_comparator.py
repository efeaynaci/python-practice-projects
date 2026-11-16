import math


def ask_quantity(supplier):
    while True:
        try:
            quantity = int(input(f"Enter Supplier {supplier} quantity: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if quantity > 0:
            return quantity

        print("Quantity must be greater than zero.")


def ask_price(supplier):
    while True:
        try:
            price = float(input(f"Enter Supplier {supplier} total price: "))
        except ValueError:
            print("Please enter a valid price.")
            continue

        if math.isfinite(price) and price >= 0:
            return price

        print("Please enter a valid price of zero or more.")


quantity_a = ask_quantity("A")
price_a = ask_price("A")
cost_per_item_a = price_a / quantity_a
print("Supplier A cost per item:", cost_per_item_a)

quantity_b = ask_quantity("B")
price_b = ask_price("B")
cost_per_item_b = price_b / quantity_b
print("Supplier B cost per item:", cost_per_item_b)

if cost_per_item_a < cost_per_item_b:
    print("Supplier A is cheaper.")
elif cost_per_item_b < cost_per_item_a:
    print("Supplier B is cheaper.")
else:
    print("Both suppliers have the same cost per item.")