def generate_pattern(n, reverse=False):
    if reverse:
        for i in range(n, 0, -1):
            print('*' * i)
    else:
        for i in range(1, n + 1):
            print('*' * i)

def get_input():
    n = int(input("Enter the number of rows for the pattern: "))
    reverse_option = input("Do you want to print the pattern in reverse? (yes/no): ")
    reverse = reverse_option == 'yes'
    return n, reverse

def main():
    n, reverse = get_input()
    generate_pattern(n, reverse)

main()
