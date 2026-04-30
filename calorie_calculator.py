# Function to calculate BMR
def calculate_bmr(weight, height, age, gender):
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == "female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Invalid gender. Please enter 'male' or 'female'.")
    return bmr

# Taking user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))
age = int(input("Enter your age in years: "))
gender = input("Enter your gender (male/female): ")

# Calculating BMR
bmr = calculate_bmr(weight, height, age, gender)

# Showing result
print(f"\nYour Basal Metabolic Rate (BMR) is: {bmr:.2f} calories/day.")

# Optional: Estimate daily calories for different activity levels
print("\nEstimated daily calorie needs based on activity level:")
print(f" - Sedentary (little/no exercise): {bmr * 1.2:.0f} calories/day")
print(f" - Lightly active (1–3 days/week): {bmr * 1.375:.0f} calories/day")
print(f" - Moderately active (3–5 days/week): {bmr * 1.55:.0f} calories/day")
print(f" - Very active (6–7 days/week): {bmr * 1.725:.0f} calories/day")
print(f" - Super active (twice daily training): {bmr * 1.9:.0f} calories/day")
