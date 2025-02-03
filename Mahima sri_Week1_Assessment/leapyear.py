
def get_input():
    years = input("Enter years : ")
    return list(map(int, years.split()))

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def main():
    years = get_input()
    for year in years:
        if is_leap_year(year):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
main()