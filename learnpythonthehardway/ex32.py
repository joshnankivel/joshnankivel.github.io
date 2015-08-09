the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i

print elements

# make a new list to play with
playlist = []
for i in range(0,10):
	playlist.append(i + 1)

print playlist	

print "How long is this thing? %r items." % len(playlist)

playlist2 = playlist + playlist

print "\n\nWhen you add it to itself it looks like this:\n%r" % playlist2

playlist3 = playlist * 4

print "\n\nWhen you multiply the list by 4 this is what it looks like:\n%r" % playlist3

# this doesn't work properly for some reason, maybe can't put a boolean directly into a string.
print "Why does this say: %r about 42 being in playlist?" % 42 in playlist

print "When this is the truth of it:", 42 in playlist, "?"

print "Let's try slicing playlist[3:]: ", playlist[3:]

print "Let's compare two lists: cmp(playlist, playlist2): ", 	cmp(playlist, playlist2)

print "What's the max value in playlist? ", max(playlist)

print "What's the min value in playlist? ", min(playlist)