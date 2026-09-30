# main.py - Fitness App

print("Welcome to Fitness Tracker!")

name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height * height)

print(f"\nHi {name}, Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are Underweight - Konjam saapdu ma!")
elif bmi < 24.9:
    print("You are Fit - Super!")
else:
    print("You are Overweight - Workout pannu!")
