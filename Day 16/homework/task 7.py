#7) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს საჭმელების list'ს და გამოიტანს ყველას ცალ-ცალკე

def print_foods(food_list):
  
    for food in food_list:
        print(food)


my_foods = ["Pizza", "Sushi", "Burger", "Pasta"]
print_foods(my_foods)
