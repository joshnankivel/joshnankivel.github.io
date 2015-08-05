from sys import argv

script, filename = argv

filecontents = open(filename)
print filecontents.read()