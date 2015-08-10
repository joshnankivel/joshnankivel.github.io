def looptimes(stop_after, increment_by):
	i = 0
	numbers = []

	while i < stop_after:
		print "At the top i is %d" % i
		numbers.append(i)

		i += increment_by
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i


	print "The numbers: "

	for num in numbers:
		print num

print looptimes(6,2)