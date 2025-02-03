
def get_input():
    number = int(input("Enter a number : "))
    
    range_limit = int(input("Enter the range: "))
    return number,range_limit

def multiplication_table(number, range_limit):
    table = []
    for i in range(1, range_limit + 1):
        table.append(f"{number} * {i} = {number * i}")
    return table

def display_table(table):
    for j in table:
        print(j)

def main():
    number ,range_limit = get_input()
    table = multiplication_table(number, range_limit)
    print(f"Multiplication table for {number}:")
    display_table(table)

main()