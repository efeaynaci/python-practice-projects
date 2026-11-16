def exit_loop():
    while True:
        word = input("Enter the the word: ")
        if word == "exit" or  word == "Exit" or  word == "EXIT":
            print("Goodbye!")
            break 
        else:
            print("Try again")
            continue


exit_loop()