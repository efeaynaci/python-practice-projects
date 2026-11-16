def ask_quantity():
    while True:
        try:
            number = int(input("Enter a whole number: "))

        except ValueError:
            print("Please enter a whole number.")
            continue
        if number <= 0:
            print("Quantity must be greater than zero.")
            continue 
        
        return number

print(ask_quantity())
        