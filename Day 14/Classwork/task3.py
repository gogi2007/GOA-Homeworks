#3) გადააკოპირეთ ეს list'ი:

#listn = ["good", "is", "programming"]

#ამ list'ის მეშვეობით გამოიტანეთ წინადადება: "programming is good", ჯერ დადებითი, შემდეგ კი უარყოფითი ინდექსებით 



listn = ["good", "is", "programming"]


sentence_positive = f"{listn[2]} {listn[1]} {listn[0]}"
print("Using positive indices:", sentence_positive)


sentence_negative = f"{listn[-1]} {listn[-2]} {listn[-3]}"
print("Using negative indices:", sentence_negative)
