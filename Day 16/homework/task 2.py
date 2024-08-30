#2) შექმენით ფუნქცია რომელიც არგუმენტებად მიიღებს range()'ის არგუმენტებს (start'ს და end'ს) და გამოატანინეთ რიცხვები პირველი რიცხვიდან მეორე რიცხვამდე for loop'ის მეშვეობით

def print_range(start, end):
    
    for number in range(start, end + 1):
        print(number)


print_range(1, 5)
