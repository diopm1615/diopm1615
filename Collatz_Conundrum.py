# This program try to demonstrate the Collatz Conundrum.

from math import remainder
import random
 
# Pick any number. If it's odd,  .


# Set a counter to zero.
count = 0

# Generate a random number.
num = random.getrandbits(10)

while count != 1:

    # Check if the picked number is odd or even.
    num2 = num % 2

    # If it’s even, divide it by 2.
    if num2 == 0:

        num = num /2

    else:
        # multiply it by 3 and add 1.
        num = (num * 3) + 1

        print(num)

        
        
        





