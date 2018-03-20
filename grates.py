purple = '\033[95m'

blue = '\033[94m'

green = '\033[92m'

yellow = '\033[93m'

red = '\033[91m'

reset = '\033[0m'


grade = float (raw_input ("Pleace enter you grade on the quize. "))

if (grade >= 90.0 and grade < 100):

	print (blue + "You got an A. ")

if (grade >= 80.0 and grade < 90.0):

	print (green + "You got an B. ")

if (grade >= 70.0 and grade < 80.0):

	print (purple + "You got an C. ")

if (grade >= 60.0 and grade < 70.0):

        print (yellow + "You got an D. ")

if (grade >= 50.0 and grade < 60.0):

        print (red + "You got an E. ")

else:

	print (reset)
