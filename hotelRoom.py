month = input()
nights = int(input())

studio_price = 0
apartment_price = 0

if month in ["May", "October"]:
    studio_price = 50 * nights
    apartment_price = 65 * nights
    if nights > 14:
        studio_price *= 0.70  # 30% discount
        apartment_price *= 0.90  # 10% discount
    elif 7 < nights <= 14:
        studio_price *= 0.95  # 5% discount
elif month in ["June", "September"]:
    studio_price = 75.20 * nights
    apartment_price = 68.70 * nights
    if nights > 14:
        studio_price *= 0.80  # 20% discount
        apartment_price *= 0.90  # 10% discount
else:  # July and August
    studio_price = 76 * nights
    apartment_price = 77 * nights
    if nights > 14:
        apartment_price *= 0.90  # 10% discount

print(f"Apartment: {apartment_price:.2f} USD.")
print(f"Studio: {studio_price:.2f} USD.")
