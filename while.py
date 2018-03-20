#loopCount = 0

#index = 10

#while (index > loopCount):

#	print (index)

#	index = index - 1


secret = 7

number = 5

name = ""

while (number != secret and name.lower() == "pan"):

	print ("What is your name?")

	name = raw_input (">")

	print ("Guess my number between 0 to 10. ")

	number = int( raw_input">")

	if (number < secret):

		print ("Your number is too low.")

	elif (number > secret):

		print ("Your number is too high.")
