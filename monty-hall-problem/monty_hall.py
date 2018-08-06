# The Monty Hall Problem:
# you're presented with 3 doors, behind two of them there are goats,
# behind the other there is a car, your given a chance to choose one 
# door, but before they open the door, the presenter always opens a 
# door which holds one of the goats. now your given a chance to switch
# the door you chose, the question is should you always switch or stick
# with your first choice.
# the answer is, also it may seem counterintuitive, you should always
# switch the door. because, the probability of you choosing a goat at first
# shot is 2/3, if you stick with your initial choice no matter what presenter
# does you're going to get a goat 2 times out of 3 strikes. but because presenter
# always opens a door with a goat, and because it is more likely that you have
# chosen a door with a goat behind it, it more likely that the door left holds
# the car. in swapping you effectively swapping the probabilities of choosing
# goat and car, by swapping you'll get a car with 2/3 probabilty.
#
# author: cs0uth @ <saeid.aliei@gmail.com>

from datetime import datetime
from sys import argv
import numpy as np

def play(nplay, stick=True):
	# play nplay times and return results
	# goat:0, car:1
	chcs = []
	if stick:
		drs = [0, 0, 1]
		for _ in range(nplay):
			chc = np.random.choice(drs)
			chcs.append(chc)
	if not stick:
		for _ in range(nplay):
			drs = [0, 0, 1]
			idx = np.random.choice(range(len(drs)))
			del drs[idx]
			drs.remove(0)
			chcs.append(drs[0])

	return chcs

def main():
	try:
		nplay = int(argv[1])
	except IndexError:
		print("\nUsage: python monty_hall.py <number-of-plays>\n")
		exit()
	ini = datetime.now()
	stChcs = play(nplay, stick=True)
	swChcs = play(nplay, stick=False)
	# number of cars (1's) in stick and switch mode
	ncarSt = np.count_nonzero(stChcs)
	ncarSw = np.count_nonzero(swChcs)
	fin = datetime.now()

	print("\nNumber of games played: {}" .format(nplay))
	print("\nPercentage of car wins if you stick with initial choice: {}" .format((ncarSt*100)/nplay))
	print("Percentage of car wins if you switch from initial choice: {}" .format((ncarSw*100)/nplay))
	print("\nTime took to play: {} (s).\n" .format(fin-ini))

if __name__ == '__main__':
	main()