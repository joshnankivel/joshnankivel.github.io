from sys import argv

script, write_file = argv

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

out_file = open(write_file, 'w')
out_file.write("%s\n%s\n%s\n" % (line1, line2, line3)) 

out_file.close()