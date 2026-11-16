while True:
    try:
        number = int(input("Enter a whole number: "))

    except ValueError:
        print("Please enter a whole number.")
        continue
    print(number)
    break