def analyze_string(input_string):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    count_vowels = 0
    count_consonants = 0
    count_digits = 0
    count_special = 0

    for char in input_string:
        if char in vowels:
            count_vowels += 1
        elif char in consonants:
            count_consonants += 1
        elif char.isdigit():
            count_digits += 1
        elif not char.isspace():
            count_special += 1

    reversed_string = input_string[::-1]

    print(f"Vowels: {count_vowels}")
    print(f"Consonants: {count_consonants}")
    print(f"Digits: {count_digits}")
    print(f"Special Characters: {count_special}")
    print(f"Reversed String: {reversed_string}")

def main():
    user_input = input("Enter a string to analyze: ")
    analyze_string(user_input)

main()
