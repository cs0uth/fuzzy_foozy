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

import numpy as np

NPLAY = 100000

def play(nplay=NPLAY, stick=True):
	chcs = []
	if stick:
		drs = [0, 0, 1]
		for _ in range(nplay):
			np.random.shuffle(drs)
			chc = np.random.choice(drs)
			chcs.append(chc)
	if not stick:
		for _ in range(nplay):
			drs = [0, 0, 1]
			np.random.shuffle(drs)
			idx = np.random.choice(range(len(drs)))
			del drs[idx]
			drs.remove(0)
			chcs.append(drs[0])

	return chcs


def main():
	stChcs = play(stick=True)
	swChcs = play(stick=False)

	# number of cars(1) in stick mode
	ncarSt = np.count_nonzero(stChcs)

	# number of cars in switch mode
	ncarSw = np.count_nonzero(swChcs)

	print("\nStatistics after {} plays:" .format(NPLAY))
	print("\nPercentage of car wins if you stick with initial choice: {}" .format((ncarSt*100)/NPLAY))
	print("Percentage of car wins if you switch from initial choice: {}" .format((ncarSw*100)/NPLAY))

if __name__ == '__main__':
	main()
