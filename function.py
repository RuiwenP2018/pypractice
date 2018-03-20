GREEN = '\033[92m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
YELLOW = '\033[93m'
GREY = '\033[90m'
RED = '\033[91m'
RESET = '\033[0m'


#def is just a creating a code. def = define
def printred (message):

	print (RED + message + RESET)

def printgreen (message):

	print (GREEN + message + RESET)

def printyellow (message):

	print ()

	print (YELLOW + message + RESET)

	print ()

def printrgy (message):

	letterIndex = 0

	newmessage = ""

	while (letterIndex < len(message)):

		if (letterIndex % 3 == 0):

			newmessage += RED

		elif (letterIndex % 3 == 1):

			newmessage += GREEN

		elif (letterIndex % 3 == 2):

			newmessage += YELLOW

		newmessage = newmessage + message [letterIndex]

		letterIndex += 1

	print (newmessage + RESET)

#now we have the code, juse continue to normal coding.
for x in range (10):

	printyellow ("hello")

	printyellow ("goodbye")

#print the color red green yellow letter
printrgy ("Enter rainbow road, you will never come out in first place.")
