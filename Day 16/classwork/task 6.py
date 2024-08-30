def check_passed(score):
    if 1 <= score < 101:  
        return "Passed" if score > 80 else "Not Passed"
    return "Invalid score"


score = int(input("Enter your score (1 to 100): "))
print(check_passed(score))
