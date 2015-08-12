
# start() __ mine()_____ deep_________dead("Fell into lava")
# 		|			|_ shallow______stone
# 		|
# 		__ hunt()_____ pigs_________eat()
# 		|			|_ sheep________eat()
# 		|			|_ zombies______dead("Zombie ate your brains")
# 		|
# 		__ chop()_____ replant______carpenter
# 		|			|_ clearcut_____dead("Wood nymphs attacked and killed you")
# 		|
# 		__ farm()_____ wheat________eat()
# 		|			|_ sugar cane___dead("Starved to death on sugar")
# 		|
# 		__ build()_____ house_______protected()
# 					|_ statue_______dead("skeleton shot you full of arrows")

from sys import exit
from difflib import SequenceMatcher

def dead(why):
	print "#### ", why, "We will miss you. ####"
	exit(0)

def start():
	print "Welcome to the Minecraft Choice game!"
	print "\n\nWhat do you want to do?\n\tmine\n\thunt\n\tchop\n\tfarm\n\tbuild"

	choice = raw_input("> ")

	if choice == "mine":
		mine()
	elif choice == "hunt":
		hunt()
	elif choice == "chop":
		chop()
	elif choice == "farm":
		farm()
	elif choice == "build":
		build()
	else:
		print "I don't know what that means! Try again."

def mine():
	print "So you want to mine, eh?"
	print "Do you want to mine shallow or deep?"

	choice = raw_input("> ")

	if choice == "deep":
		dead("You mined too deep and tried to swim in lava!")
	elif choice == "shallow":
		print "You mined some stone and can craft a furnace and tools. Great job!"
	else:
		print "I don't know what that means! Try again."

def hunt():
	print "So you want to hunt, eh?"
	print "Do you want to hunt pigs, sheep, or zombies?"

	choice = raw_input("> ")

	if choice == "zombies":
		dead("You tried to hunt zombies without a sword or armor, and they ate your brains.")
	elif choice in ["pigs","sheep"]:
		print "You killed them with your bare hands, barbarian! But you are now full. Great job!"
	else:
		print "I don't know what that means! Try again."

def chop():
	print "So you want to chop down some trees, eh?"
	print "Do you want to replant or clearcut?"

	choice = raw_input("> ")

	if choice == "clearcut":
		dead("Enemy of the environment! Angry tree nyphs chewed your legs off.")
	elif choice == "replant":
		print "Renewing the natural resources is awesome, great job!"
	else:
		print "I don't know what that means! Try again."

def farm():
	print "Hello farmer brown!"
	print "Do you want to grow wheat or sugar cane?"

	choice = raw_input("> ")

	if choice == "sugar cane":
		dead("Really? You can't live on just sugar. You died of a sweet tooth.")
	elif choice == "wheat":
		print "Nice choice. You are soon making bread and having a great time."
	else:
		print "I don't know what that means! Try again."

def build():
	print "So you want to build some stuff right away, eh?"
	print "Do you want to build a house or a statue of Mickey Mouse?"

	choice = raw_input("> ")

	# using FuzzyWuzzy for fuzzy string matching, assume a match if > 50% similar
	if SequenceMatcher(None, choice, "Mickey Mouse").ratio() > .5 or SequenceMatcher(None, choice, "statue").ratio() > .5:
		dead("Wow, that will protect you from the weather and monsters. Ooops, you were attacked by monsters and died in your sleep.")
	elif choice == "house":
		print "Nice house! That will keep the rain and monsters out."
	else:
		print "I don't know what that means! Try again."

start()