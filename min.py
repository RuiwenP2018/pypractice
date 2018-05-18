def min(nums):

	smallest = nums[0]

	for candidate in nums:

		if (candidate < smallest):

			smallest = candidate

	return smallest



#list_of_numbers = (5,1,6,8,3,4,9,-5)

#print (min(list_of_numbers))

