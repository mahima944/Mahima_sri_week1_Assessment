
def get_input():
    total_bill = float(input("Enter the total bill amount: "))
    num_people = int(input("Enter the number of people: "))
    tip_percentage = float(input("Enter the tip percentage: "))
    return total_bill, num_people, tip_percentage

def split_bill(total_bill, num_people, tip_percentage):
    tip_amount = total_bill * (tip_percentage / 100)
    total_amount = total_bill + tip_amount
    amount_per_person = total_amount / num_people
    return amount_per_person

def main():
    total_bill, num_people, tip_percentage = get_input()
    amount_per_person = split_bill(total_bill, num_people, tip_percentage)
    print(f"Each person has to pay: {amount_per_person:.2f}")

main()
