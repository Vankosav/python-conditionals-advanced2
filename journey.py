budget = float(input())
season = input().lower()

destination = ""
holiday_type = ""
money_spent = 0

if budget <= 100:
    destination = "Serbia"
    if season == "summer":
        holiday_type = "Camp"
        money_spent = budget * 0.30
    elif season == "winter":
        holiday_type = "Hotel"
        money_spent = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        holiday_type = "Camp"
        money_spent = budget * 0.40
    elif season == "winter":
        holiday_type = "Hotel"
        money_spent = budget * 0.80
else:
    destination = "Europe"
    holiday_type = "Hotel"
    money_spent = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{holiday_type} - {money_spent:.2f}")


