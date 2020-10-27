"""
    Problem Statement: To print numbers between 1 and 100 according to some rules which are mentioned below:
    - print fizz for multiples of 3
    - print buzz for multiples of 5
    - print fizzbuzz for their common multiples
    - print number otherwise
"""


def check_num(number):
    if number % 3 == 0 and number % 5 == 0:  # if number variable is divisible by both 3 and 5 then print
        print("FizzBuzz")
    elif number % 3 == 0:  # checks divisibility with 3
        print("Fizz")
    elif number % 5 == 0:  # checks divisibility with 5
        print("Buzz")
    else:  # if no above condition is satisfied then print number
        print(number)


def print_fizz_nums(start: int, end: int):  # this means it only takes integer as parameters
    if start == end:  # this is the stop condition of recursion which must be there whenever using recursion
        return
  
    start += 1  # since I started with 0 incrementing it by 1
    check_num(start)  # this will evaluate the value of the "start" and print according to the condition stated
    print_fizz_nums(start, end)  # recursion function calling itself


if __name__ == '__main__':
    # initialise the start and end number between which we want to print
    end_number = 100
    start_number = 0
    # call the function and pass parameters required
    print_fizz_nums(start_number, end_number)
