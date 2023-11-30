'''
Problem 2:
Mrs Jane considers a number to be "beautiful" if all its digits are the same and not equal to zero (e.g., 333, 5, 44). Given a number x that is not divisible by 2 and not divisible by 5 (in other words, relatively prime with 10), create a program that takes input x and returns the smallest beautiful number that is divisible by x.

Example 1:

Input x: 7

The smallest beautiful number divisible by 7 is 7.

Example 2:

Input x: 13

The smallest beautiful number divisible by 13 is 111111.

Example 3:

Input x: 259

The smallest beautiful number divisible by 259 is 777.
'''
def is_beautiful(number):
    # Check if all digits are the same and not equal to zero
    return len(set(str(number))) == 1 and '0' not in str(number)

def find_smallest_beautiful_number(x):
    # Start from x and check multiples until a beautiful number is found
    multiple = x
    while not is_beautiful(multiple):
        multiple += x
    return multiple

def main():
    try:
        x = int(input("Enter a number (not divisible by 2 and 5): "))
        if x % 2 != 0 and x % 5 != 0:
            result = find_smallest_beautiful_number(x)
            print(f"The smallest beautiful number divisible by {x} is: {result}")
        else:
            print("Please enter a number that is not divisible by 2 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if _name_ == "_main_":
    main()
    main()


