# The purpose of this script is to find the maximum prime numbers for 5 seconds

import time
import sys
# Record the start time
start = time.time()

# Initialize a counter to 2
num = 1
result = []

# Infinite loop to simulate a long-running process, check every number if prime
while True:

    # Increment the number to check
    num += 1

    # Exit after 5 seconds
    if time.time() - start > 5:
        print("Finish", len(result))
        print("The last from the List: ", result[-1])
        sys.exit()
    
    # Check if the number is prime
    for i in range(2,num):
        if num % i == 0:
            break
    
    # The remaining numbers are prime, add to the list
    else:
        result.append(num)