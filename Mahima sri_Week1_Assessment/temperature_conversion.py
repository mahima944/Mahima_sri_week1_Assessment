def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    

    choice = int(input("Choose a conversion (1-6): "))
    
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F")
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_kelvin(celsius)}K")
    elif choice == 3:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C")
    elif choice == 4:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_kelvin(fahrenheit)}K")
    elif choice == 5:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin}K = {kelvin_to_celsius(kelvin)}°C")
    elif choice == 6:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin}K = {kelvin_to_fahrenheit(kelvin)}°F")
    else:
        print("Invalid choice. Please select a number between 1 and 6.")


main()
