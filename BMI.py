name = "gulzar"
height_m = 1.59
weight_kg = 62.80

bmi = weight_kg / (height_m ** 2)
print("bmi: ")
print(bmi)
if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")
