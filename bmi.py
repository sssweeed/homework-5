def calculate_bmi(weight, height):
"""Calculate Body Mass Index (BMI)."""
height_m = height / 100
bmi = weight / (height_m ** 2)

print("\n=== BODY MASS INDEX ===")
print(f"Your BMI: {bmi:.1f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obesity")

return bmi
