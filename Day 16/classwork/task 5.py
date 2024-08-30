#5) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს მომხმარებლის ასაკს და გამოიტანს სრულწლოვანია თუ არა

def is_of_legal_age(age):
    return age >= 18


age = int(input("Enter your age "))
if is_of_legal_age(age):
    print("You are of legal age.")
else:
    print("You are not of legal age.")

