#2) შექმენით list'ი 15 ელემენტით, დაუწერეთ ინდექსების კომენტარები და შემდეგ ცალ-ცალკე გამოიტანეთ ყველა ჯერ დადებითი, შემდეგ კი უარყოფითი ინდექსებით


my_list = [
    'a',  # Index 0
    'b',  # Index 1
    'c',  # Index 2
    'd',  # Index 3
    'e',  # Index 4
    'f',  # Index 5
    'g',  # Index 6
    'h',  # Index 7
    'i',  # Index 8
    'j',  # Index 9
    'k',  # Index 10
    'l',  # Index 11
    'm',  # Index 12
    'n',  # Index 13
    'o'   # Index 14
]


print("Complete List:")
print(my_list)


print("\nElements accessed with positive indices:")
for i in range(len(my_list)):
    print(f"Element at index {i}:", my_list[i])


print("\nElements accessed with negative indices:")
for i in range(-len(my_list), 0):
    print(f"Element at index {i}:", my_list[i])
