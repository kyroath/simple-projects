"""

Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead
of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five
print “FizzBuzz”.

"""

for i in range(1,101):

    flag_three = False
    flag_five = False

    if i % 3 == 0:
        print("Fizz", end='')
        flag_three = True
    if i % 5 == 0:
        print("Buzz", end='')
        flag_five = True
    if not flag_three and not flag_five:
        print(i, end='')
    print()

