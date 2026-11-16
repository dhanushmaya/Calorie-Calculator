print("--- Daily Calorie Calculator ---")

gender = input("Gender (m/f): ").strip().lower()
age = int(input("Age: "))
weight = float(input("Weight (kg): "))
height = float(input("Height (cm): "))

print("\nActivity Level:")
print("1 - Sedentary (desk job, no workout)")
print("2 - Light (1-3 workouts a week)")
print("3 - Moderate (3-5 workouts a week)")
print("4 - Active (6-7 workouts a week)")
activity = input("Pick 1-4: ").strip()

# Mifflin-St Jeor formula for BMR
if gender == "m":
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
elif gender == "f":
    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
else:
    print("Invalid gender entered. Please use 'm' or 'f'.")
    exit()

# Multiply BMR by activity factor
if activity == "1":
    tdee = bmr * 1.2
elif activity == "2":
    tdee = bmr * 1.375
elif activity == "3":
    tdee = bmr * 1.55
elif activity == "4":
    tdee = bmr * 1.725
else:
    print("Invalid choice, defaulting to sedentary.")
    tdee = bmr * 1.2

# Basic 30/40/30 macro split
protein = round((tdee * 0.30) / 4)
carbs = round((tdee * 0.40) / 4)
fats = round((tdee * 0.30) / 9)

print("\n--- Results ---")
print(f"BMR: {round(bmr)} kcal/day")
print(f"Maintenance (TDEE): {round(tdee)} kcal/day")
print(f"Weight Loss (-300): {round(tdee - 300)} kcal/day")
print(f"Weight Gain (+300): {round(tdee + 300)} kcal/day")
print(f"\nMacros for maintenance: {protein}g Protein | {carbs}g Carbs | {fats}g Fat")
