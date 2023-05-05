import random
import matplotlib.pyplot as plt

def monty_hall(n_trials):
    switch_wins = 0
    stay_wins = 0
    doors = ['car', 'goat', 'goat']
    for i in range(n_trials):
        random.shuffle(doors)
        chosen_door = random.randint(0, 2)
        if doors[chosen_door] == 'car':
            stay_wins += 1
        else:
            switch_wins += 1
    return stay_wins, switch_wins

n_trials = 10000
stay_wins, switch_wins = monty_hall(n_trials)

plt.pie([stay_wins, switch_wins], labels=["Stay Wins", "Switch Wins"])
plt.axis('equal')
plt.title("Monty Hall Problem")
plt.show()
