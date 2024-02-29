groupBudget = int(input())
season = input()
numFisherman = int(input())
cost = 0
discount = 0

if season == "Spring":
    cost = 3000
    if numFisherman <= 6:
        discount = cost * 0.10
    elif 7 <= numFisherman <= 11:
        discount = cost * 0.15
    elif numFisherman > 12:
        discount = cost * 0.25
elif season in ["Summer", "Autumn"]:
    cost = 4200
    if numFisherman <= 6:
        discount = cost * 0.10
    elif 7 <= numFisherman <= 11:
        discount = cost * 0.15
    elif numFisherman > 12:
        discount = cost * 0.25
elif season == "Winter":
    cost = 2600
    if numFisherman <= 6:
        discount = cost * 0.10
    elif 7 <= numFisherman <= 11:
        discount = cost * 0.15
    elif numFisherman > 12:
        discount = cost * 0.25

if numFisherman % 2 == 0 and season in ["Summer", "Spring", "Winter"]:
    discount += cost * 0.05

cost -= discount
remainingAmount = groupBudget - cost

if remainingAmount >= 0:
    print(f"Yes! You have {remainingAmount:.2f} USD left.")
else:
    need = abs(remainingAmount)
    print(f"Not enough money! You need {need:.2f} USD.")
