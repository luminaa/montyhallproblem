# Monty Hall Problem Simulation

This is a simulation of the famous Monty Hall Problem from the show "Let's Make a Deal". 

## What is the Monty Hall problem?

The problem is based on a game show scenario in which a contestant is asked to choose one of three doors. Behind one of the doors is a prize, while the other two doors conceal goats.

After the contestant has made their initial choice, the host, who knows what is behind each door, opens one of the other two doors to reveal a goat. The contestant is then given the option to either stick with their initial choice or switch to the other unopened door.

The question is: What is the best strategy for the contestant? Should they stick with their initial choice or switch to the other unopened door?

## Simulation 

`monty_hall.py` simulates the game show scenario by randomly assigning a prize and two goats behind the three doors, shuffling the doors, and then choosing one door at random as the contestant's initial choice.

The program then checks whether the chosen door contains the prize or a goat. If the contestant chooses the door with the prize, they win if they stay with their initial choice; if they choose a door with a goat, they win if they switch to the other unopened door. The program repeats this process a specified number of times, and returns the number of wins for each strategy (staying or switching).

## Outcome

The simulation will be represented in a pie chart as seen below: 

![pie chart of the outcome](piechartpng) 

The results of the simulation may be counterintuitive: despite seeming to have a 50-50 chance of winning by staying or switching, switching doors actually gives the contestant a better chance of winning. 

To understand why switching doors gives the contestant a better chance of winning, we can use Bayes' theorem. Bayes' theorem is a fundamental concept in probability theory that allows us to update our beliefs about an event based on new information. Bayes' theorem involves two key concepts: likelihood and prior probability. The likelihood is the probability of observing the evidence given a particular hypothesis. In the Monty Hall problem, the evidence is the host revealing a goat. The prior probability is the initial probability of the hypothesis being true before the evidence is observed. In the Monty Hall problem, the prior probability of each door containing the prize is 1/3.

If the contestant stays with their initial choice, their probability of winning is 1/3, since there are three equally likely possibilities at the start, and only one of them is a winning door. If they switch, their probability of winning is the probability that the other unopened door contains the prize, which is 2/3, since we know that one of the two remaining doors must be a goat.

Therefore, switching doors gives the contestant a higher chance of winning. This may seem counterintuitive, but it can be explained by Bayes' theorem, which allows us to update our beliefs based on new information. In the Monty Hall problem, the host's action of revealing a goat provides new information that changes the probabilities of the remaining doors.