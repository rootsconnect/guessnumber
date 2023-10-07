import random
from math import log

def randomnumbergame(start,end):
	max_guess_base = end-start
	max_guess = log(max_guess_base) * 1.5
	number = random.randint(start, end)
	enter = 0
	counter = 0
	
	while number != enter:
		counter = counter + 1
		enter = input("\nGuess Number: ")
		if number < enter:
			print "lower!"
		if number > enter:
			print "higher!"
		if counter > max_guess:
			print "you guessed too much! - exiting"
			return 0

	print("You are the best!")
	print "You tried ", counter, " times!  The max would be ", int(max_guess)


print("##Guess a random Number Game###")
start = input("Enter a start number: ")
end = input("Enter a end number: ")
print "Guess a number between ", start, " and ", end

randomnumbergame(start, end)