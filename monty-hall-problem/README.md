### Monty Hall Problem:
You're presented with 3 doors in a game show, behind two of them there are 2 goats and behind the other one there is a car, now your given a shot to choose a door, whatever is behind it, you'll get that as a prize, well you'll naturally want the new, shiny car!
now before they open the door, the game show host always opens a door with a goat and you're given a chance to switch the door you initially chose.

What is the best strategy in the long run:  
1. Stick with your initial choice.  
2. Always switch the door.  
3. doesn't matter.

although it may seem counterintuitive if you always switch, it is far better than if you stick with your initial choice. why?  
well because the probability of you choosing a goat at first shot is 2/3. but since the host **always** opens a door with a goat behind it, it is more likely that the door left holds the car. In swapping you effectively swapping the probabilities for getting a car and a goat. run the program to see for yourself!

```
Number of games played: 100000

Percentage of car wins if you stick with initial choice: 33.411
Percentage of car wins if you switch from initial choice: 66.56

Time took to play: 0:00:02.263888 (s).
```

To read more about it refer to Wikipedia's page:
[Monty Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)
