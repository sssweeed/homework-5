def calculate_calories():
    print("=== CALORIE CALCULATOR ===")

    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))

    gender = input("Enter your gender (male/female): ").lower()

    print("\nActivity levels:")
    print("1 - Sedentary")
    print("2 - Lightly active")
    print("3 - Moderately active")
    print("4 - Very active")
    print("5 - Extra active")
    activity = int(input("Choose activity level (1-5): "))

    activity_factors = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.9
    }

    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == "female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        print("Invalid gender.")
        return

    if activity not in activity_factors:
        print("Invalid activity level.")
        return

    tdee = bmr * activity_factors[activity]

    print("\n=== YOUR RESULTS ===")
    print(f"BMR: {bmr:.0f} kcal")
    print(f"Maintenance calories: {tdee:.0f} kcal")
    print(f"Weight loss target: {tdee - 300:.0f} kcal")
    print(f"Weight gain target: {tdee + 300:.0f} kcal")

    protein = weight * 1.6
    fats = weight * 0.9
    carbs = (tdee - protein * 4 - fats * 9) / 4

    print("\n=== DAILY MACRONUTRIENTS ===")
    print(f"Protein: {protein:.0f} g")
    print(f"Fats: {fats:.0f} g")
    print(f"Carbohydrates: {carbs:.0f} g")
