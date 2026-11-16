def letter_grade():
    exam_1=(float(input("Enter the first exam score: ")))
    exam_2=(float(input("Enter the second exam score: ")))
    average= (exam_1+exam_2) / 2
    if average >= 90:
        letter_grade="A"
    elif 90 > average >= 80:
        letter_grade="B"
    elif 80 > average >= 70:
        letter_grade="C"
    elif 70 > average >= 60:
        letter_grade="D"
    elif 60 > average:
        letter_grade="F"

    print("Your average score is: ",average)
    print("The letter grade is: ",letter_grade)
letter_grade()

