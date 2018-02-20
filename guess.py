#to do, change to random number

import random

answer = random.randint(0,5)

guess = int(raw_input ("Enter a number, 0-5: "))

print (answer,guess)

if (guess > answer):

	print ("Your number is too big.")

	guess = int (raw_input ("Enter a number, 0-5: "))

	if (guess > answer):

		print ("Your number is still too high.")

	elif (guess < answer):

		print ("Your number is still too low.")

	elif (guess == answer):

		print ("You got it, nice work.")

elif (guess < answer):

	print ("Your number is too low.")

        guess = int (raw_input ("Enter a number, 0-5: "))

        if (guess > answer):

                print ("Your number is still too high.")

        elif (guess < answer):

                print ("Your number is still too low.")

        elif (guess == answer):

                print ("You got it, nice work.")

elif (guess == answer):

	print ("Yes, you guessed my number.")

else:

	print ("Too bad, you are wrong..... You need to give me a number 0-5")
