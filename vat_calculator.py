amount_before_vat = float(input("Enter the amount before VAT: "))

while True:
    try:
        vat_rate = float(input("Enter the VAT rate: "))
    except ValueError:
        print("Invalid VAT rate.")
        continue
    if 0 <= vat_rate <=100:
        break
    print("Invalid VAT rate.")
vat_amount = (amount_before_vat * vat_rate) / 100
print("VAT amount: ",vat_amount)
amount_after_vat = (amount_before_vat + vat_amount)
print("Amount after VAT: ",amount_after_vat)

