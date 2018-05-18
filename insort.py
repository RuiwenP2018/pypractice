import min

import random

numbers = [random.randint (1,100) for x in range(100)]

print (numbers)

print ("\n\n\n")

ordered = []

while (len(numbers) > 0):

	smallest = min.min(numbers)

	ordered.append(smallest)

	numbers.remove(smallest)

print (ordered)
