socks = "socks"

jeans = "jeans"

laptop = "laptop"

toiletries = "toiletries"


luggage = [
"socks",
"jeans",
"laptop",
"toiletries"
]

print (luggage [1])


grades = [
96.0,
100.0,
75.5,
89.5
]

sum = 0

for grade in grades:

	sum = sum + grade

	print (sum)

#print (grades, sum(grades)/len(grades))


luggage = []

done = "n"

while (done != "y")

	item1 = raw_input("What you like to pack for a trip? ")

	luggage.append(item1)

	done = raw_input ("add another item? y/n ")

for items in luggage:

	print (items)
