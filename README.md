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

The results of the simulation may be counterintuitive: despite seeming to have a 50-50 chance of winning by staying or switching, switching doors actually gives the contestant a better chance of winning. This can be explained using Bayes' theorem, which states that the probability of an event (such as winning the prize) given some evidence (such as the host revealing a goat) is proportional to the likelihood of the evidence given the event and the prior probability of the event. In the Monty Hall problem, the evidence is the host revealing a goat, and the prior probabilities are 1/3 for each door. If the contestant stays with their initial choice, their probability of winning is 1/3. If they switch, their probability of winning is the probability that the other unopened door contains the prize, which is 2/3. Therefore, switching doors gives the contestant a higher chance of winning.
