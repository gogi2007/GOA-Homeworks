#3) შექმენით ფუნქცია რომელიც არგუმენტებად მიიღებს სახელს, გვარს, ასაკს და აკადემიას. გამოატანინეთ შემდეგი წინადადება: My name is ..., my surname is ..., I study in ....

def introduce_myself():
    
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")
    academy = input("Enter your academy: ")
    
    
    introduction = (f"My name is {first_name}, my surname is {last_name}, "
                    f"I am {age} years old, and I study in {academy}.")
    
    
    print(introduction)


introduce_myself()


