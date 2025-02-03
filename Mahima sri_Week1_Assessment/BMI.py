import math

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_input():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    return weight, height

def main():
    weight, height = get_input()
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi}")

main()
