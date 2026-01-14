marks = int(input())
attendance = int(input())
category = input()

# STEP 1: Validation
if marks < 0 or marks > 100:
    print("Invalid Marks")

elif attendance < 0 or attendance > 100:
    print("Invalid Attendance")

# STEP 2: Attendance eligibility
elif attendance < 75:
    print("Not Eligible For Exam")

else:
    # STEP 3: Result
    if marks < 35:
        print("Result: Fail")
    elif marks < 75:
        print("Result: Pass")
    else:
        print("Result: Distinction")

    # STEP 4: Grade
    if marks >= 85:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 35:
        print("Grade: C")
    else:
        print("Grade: Fail")

    # STEP 5: Admission
    if category == "general":
        if marks >= 75:
            print("Admission Granted")
        else:
            print("Admission Denied")

    elif category == "obc":
        if marks >= 70:
            print("Admission Granted")
        else:
            print("Admission Denied")

    elif category == "sc":
        if marks >= 65:
            print("Admission Granted")
        else:
            print("Admission Denied")

    else:
        print("Invalid Category")