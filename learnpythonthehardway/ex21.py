def add(a, b):
	print "ADDING %d + %d" % (a,b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

print "Now let's multiply two numbers the user wants."

var_mult = multiply(float(raw_input("First number:")), float(raw_input("Second number:")))	
print var_mult

# 7 + 8 / 10 - 37 * 42
newcalc = subtract(add(7, divide(8, 10)), multiply(37, 42))
print newcalc
print var_mult
