#6) შექმენით ფუნქცია რომელიც დააბრუნებს 3 რიცხვის ნამრავლს, შემდეგ კი დაბრუნებული მნიშვნელობა მიანიჭეთ ცვლადს

def multiply_numbers(num1, num2, num3):
    
    return num1 * num2 * num3


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))


product_result = multiply_numbers(number1, number2, number3)


print(f"The product of {number1}, {number2}, and {number3} is {product_result}.")
