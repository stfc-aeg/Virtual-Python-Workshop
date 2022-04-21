# A number is prime if it does not have any factors aside from 1 and itself. For example, 3.
# This means that one is not a prime number! 1 is its only factor, prime numbers have two factors.
# So, primes can be found by checking if every number from 2 to number-1 is a factor of number.
# You can save time by just checking up to the square root of the prime.
#    --> A composite number must have a factor less than its square root.
#    --> (It can't have two factors larger than its square root)

import math  # We'll use this for square root and rounding.

print("Let's find a prime number! WARNING: large numbers may take a long time to check.")
number = int(input("Enter a number to see if it's prime: "))

if number > 1:  # 1 is not a prime number! It has only one factor, itself.
    rangeLimit = math.ceil(math.sqrt(number))  # Math.ceil rounds up. range() likes integers.

    for i in range(2, rangeLimit):
        if number % i == 0:  # 'modulo' (%) checks how many times a number divides into another number
                          # if modulo is zero, that number is a factor of the other. e.g.: 4 % 2 = 0
            print("\n" + str(number) + " is not a prime number.")

            numStr = str(number)
            iterStr = str(i)
            pairedFactor = str(number//i)

            print(iterStr + " is a factor of " + numStr + ".")
            print(iterStr + " x " + pairedFactor + " = " + numStr)
            # An extension would be to get all factors of the number!
            break
    else:  # Make sure this else is indented to the same level as the 'for i in range' line!
           # What happens if it's indented to match the if statement following that line?
        print(str(number) + " is a prime number!")

else:
    print("1 is not a prime number.")
