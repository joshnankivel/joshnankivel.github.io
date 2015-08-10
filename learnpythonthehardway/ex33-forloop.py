def looptimes(stop_after, increment_by):
	loop_range = range(0, stop_after / increment_by)
	numbers = []
	t = 0

	for i in loop_range:
		print "At the top t is %d" % t
		numbers.append(t)

		t += increment_by
		print "Numbers now:", numbers
		print "At the bottom t is %d" % t


	print "The numbers: "

	for num in numbers:
		print num

print looptimes(6,2)