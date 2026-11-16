item_totals = []
while True:
    product = input("Enter the name of the product")
    if product == "done" or product == "Done" or product == "DONE":
        break 

    quantity = int(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: "))

    item_total = quantity * unit_price
    item_totals.append(item_total)


print("Order total: ",sum(item_totals))
