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
    n = n+1  # We increment the given number with 1 in case it is already perfect 
    while True:  # We want to make sure we can iterate through the code until we find the number
        sum_of_divisors = 1  # We initialize the sum with 1 since 1 is a proper divisor of any number
        for i in range(2, n // 2 + 1):  
            if n % i == 0:
                sum_of_divisors = sum_of_divisors + i  # We add the proper divisors to our sum

        if sum_of_divisors == n:  # In case we found the perfect number we want to break from the while loop and return n
            break
        n = n+1 # In case the number didn't pass we increment it again and reinitialize the sum with 1
    return n


def is_perfect(num):
    sum_of_divisors = 1  # Likewise, we initalize the sum with 1 for the same reason
    for i in range(2, num // 2 + 1):
        if num % i == 0:  # We search for divisors in the minimal range possible
            sum_of_divisors += i
    return sum_of_divisors == num  # We return a Boolean value for the equality given


def get_perfect_number_version_2(n):
    n += 1  # We increment the given number in case it is already a perfect number
    while True:  # We want to be able to iterate until we find the perfect number
        if is_perfect(n):
            return n
        n += 1  # In case the number incremented isn't perfect we increment it again and continue the loop


def main():

    n = get_natural_input()
    perfect_number = get_perfect_number(n)
    print("The perfect number is, ", perfect_number)


main()
