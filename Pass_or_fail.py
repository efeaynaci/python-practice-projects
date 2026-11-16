def pass_or_fail():
    exam_1=float(input("Enter the first exam score:"))
    exam_2=float(input("Enter the second exam score:"))
    average=(exam_1+exam_2) / 2
    print(average)
    if 100>= average >= 50:
        print("Passed")
    elif 50 > average >= 0:
        print("failed")
    else:
        print("Pleae enter a number between 0-100")

pass_or_fail()