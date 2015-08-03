# import module
from sys import argv
# specify arguments
script, filename = argv
# create a file object called txt from the file
txt = open(filename)

print "Here's your file %r:" % filename # print the filename
print txt.read() # print the file contents

print "Type the filename again:" #print
file_again = raw_input("> ") #prompt for file name

txt_again = open(file_again) #create a file object called txt_again from the file

print txt_again.read() # print the file contents

txt.close()
txt_again.close()
