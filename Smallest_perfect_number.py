def get_natural_input():
    while True:
        try:
            n = int(input("Enter a natural number: "))
            if n >= 0:
                return n
            else:
                print("Please enter a positive number: ")
        except ValueError:
            print("Invalid input. Please enter a natural number: ")



def get_perfect_number(n: int):
    n = n+1
    while True:
        sum_of_divisors = 1  
        for i in range(2, n // 2 + 1):  
            if n % i == 0:
                sum_of_divisors = sum_of_divisors + i

        if sum_of_divisors == n:
            break  
        n = n+1
    return n

def is_perfect(num):
    sum_of_divisors = 1  
    for i in range(2, num // 2 + 1):  
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num


def get_perfect_number_version_2(n):
    n += 1  
    while True:
        if is_perfect(n):
            return n  
        n += 1  


def main():

    n = get_natural_input()
    perfect_number = get_perfect_number(n)
    print("The perfect number is, ", perfect_number)


main()