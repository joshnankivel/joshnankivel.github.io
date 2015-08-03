formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
# print formatter % ("one", "two", "three") # this gives Error: not enough arguments for format string
# print formatter % ("one", "two", "three", "four", "five") # this gives Error: not all arguments converted during string formatting
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)