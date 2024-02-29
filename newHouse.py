typeFlower = str(input())
numFlowers = int(input())
budget = int(input())

discount = 0
cost = 0


if typeFlower == "Roses":
    cost = numFlowers * 5
    if numFlowers > 80:
        discount = cost * 0.10
elif typeFlower == "Dahlias":
    cost = numFlowers * 3.80
    if numFlowers > 90:
        discount = cost * 0.15
elif typeFlower == "Tulips":
    cost = numFlowers * 2.80
    if numFlowers > 80:
        discount = cost * 0.15
elif typeFlower == "Narcissus":
    cost = numFlowers * 3
    if numFlowers < 120:
        cost = cost * 1.15
elif typeFlower == "Gladiolus":
    cost = numFlowers * 2.50
    if numFlowers < 80:
        cost = cost * 1.20

cost -= discount
remainingAmount = budget - cost

if remainingAmount >= 0:
    print(f"Hey, you have a great garden with {numFlowers} {typeFlower} and {remainingAmount:.2f} USD left.")
else:
    need = abs(remainingAmount)
    print(f"Not enough money, you need {need:.2f} USD more.")

