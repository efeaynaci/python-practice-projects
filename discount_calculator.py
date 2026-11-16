order_total = float(input("Enter the order total: "))
print(order_total)

if order_total >= 100:
    discount_amount = order_total / 10
    order_total = (order_total * 9) / 10
    print("The discount amount is: ", discount_amount)
    print("Final total: ",order_total)
else:
    print("The discount amount is:0",)
    print("Final total: ",order_total)
