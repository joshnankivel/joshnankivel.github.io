print "Enter degrees Fahrenheit: ",
far = float(raw_input()) # had to wrap this in the float() function because it was treating it as a string

cel = round((far - 32.0) * (5.0/9.0),1) # had to change integers to floats so the output would be a float

print "%s Fahrenheit is %s Celcius." % (far, cel)