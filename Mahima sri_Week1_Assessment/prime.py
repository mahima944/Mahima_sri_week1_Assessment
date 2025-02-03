import math
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def get_input():
    start=int(input("enter start value: "))
    end=int(input("enter end value: "))
    return (start,end)

def main():
    start,end=get_input()
    print(f"prime numbers from {start} to {end} are: ")
    for i in range(start,end+1):
        if is_prime(i):
            print(i,end=" ") 
                
main()


