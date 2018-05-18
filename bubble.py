import swap


#ten = 10

#fifteen = 15

#print (ten, fifteen)

#print (swap. swap(ten, fifteen))


nums = [4, 1, 3, 8, 2]

print (nums)

x = 0

while (x < len(nums)):

	print (x, nums[x])

	if (x+1 < len(nums)):

		if (nums[x]> nums[x+1]):

			nums[x], nums[x+1] = swap.swap(nums[x], nums[x+1])

			x = 0

	x += 1

print (nums)
