def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Error: Factorial is not defined for negative numbers")
        else:
            fact = factorial(number)
            print(f"The factorial of {number} is {fact}.")
    except ValueError:
        print("Error: Please enter a valid integer.")

main()

