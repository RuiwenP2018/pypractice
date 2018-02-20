#string upper and lower case print

s = raw_input ("Pleace enter a word? ")

upper_s = s.upper()

print (upper_s)

lower_s = s.lower()

print (lower_s)

combined = upper_s +" "+ lower_s

print (combined)


#to calculate the number of the letter.

num_s = len(s)

print (num_s)

num_combined = len(combined)

print (num_combined)


#look into a letter (get the letter you want from a word)

halfway = len(s)/2

print (s[halfway])

print (s[0])

last = len(s) - 1

print (s[last])

print (s[-1])


#word slice

firsthalf = s[0:halfway]

lasthalf = s[halfway:last+1]
###can be replace by lasthalf = s[halfway:len(s)]

print ("this is the first and last half of the word.")

print (firsthalf)

print (lasthalf)

copy = s[:]

skip = s[1::2]

revers = s[0::-1]

print (revers)

print (skip)

value = s[:len(s)/2:-1]

print (value)


#count the times that the letter you put in

print (s.count("l"))



#find the letter you put in, where is it at.

print (s.find("e"))


#show all the letter up untill the letter you trying to find.

print (s[:s.find("e")])

#

words = s.split()

numberofwords = len(words)

print (words[0:2])

print (words[0:2:-1])

print (words[::-1])

sentence = "\n".join(words)

print (sentence)

newsentence = sentence.replace("\n",":-)")

print (newsentence)

#replace the words you choose

replaced = s.replace ("great" , "awesome")

print (replaced)
