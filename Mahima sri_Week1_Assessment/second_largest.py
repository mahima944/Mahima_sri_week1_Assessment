def get_input():
    user_input = input("enter a list of numbers: ")
    numbers= list(map(int, user_input.split()))
    return numbers
def get_input():
    user_input = input("Enter a list of numbers: ")
    numbers = list(map(int, user_input.split()))
    return numbers

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]


def main():
    numbers = get_input()
    second_largest = find_second_largest(numbers)
    if second_largest is not None:
        print(f"The second largest number is: {second_largest}")
    

main()

