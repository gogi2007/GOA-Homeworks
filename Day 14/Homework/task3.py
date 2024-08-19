#3) შექმენით ახალი list'ი ესეც 15 ელემენტით, slicing'ის მეშვეობით გამოიტანეთ პირველი სამი ელემენტი, მეორე სამი ელემენტი და ა.შ


alphabet_list = ['a', 'b', 'c', 'd', 'e',
                 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o']



first_three = alphabet_list[:3]
print("First three elements:", first_three)


second_three = alphabet_list[3:6]
print("Second three elements:", second_three)


third_three = alphabet_list[6:9]
print("Third three elements:", third_three)


fourth_three = alphabet_list[9:12]
print("Fourth three elements:", fourth_three)


fifth_three = alphabet_list[12:15]
print("Fifth three elements:", fifth_three)
