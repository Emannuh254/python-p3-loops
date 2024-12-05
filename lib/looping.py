def happy_new_year():
    i = 10  
    while i > 0:  
        print(i) 
        i -= 1  
    print("Happy New Year!") 


def square_integers(integers):
    return [integer ** 2 for integer in integers]


def fizzbuzz():
    for num in range(1, 101):  # Loop from 1 to 100
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")  # Multiple of both 3 and 5
        elif num % 3 == 0:
            print("Fizz")  # Multiple of 3
        elif num % 5 == 0:
            print("Buzz")  # Multiple of 5
        else:
            print(num)  # not a multiple of 3 or 5
