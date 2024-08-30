#4) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს სახელს და გვარს და გამოიტანს მისალმებას

def greet():
    
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    
    greet = (f"Hello {first_name},{last_name},!")
    

    print(greet)

greet()
