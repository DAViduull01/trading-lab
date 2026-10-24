import random
from pathlib import Path
import matplotlib.pyplot as plt

random.seed(42)
WIN_PROBABILITY = 0.55
NUM_SIMULATIONS = 10000

start_bankrolls = [5, 10, 20, 30, 50]
win_probabilities = [0.5, 0.51, 0.55, 0.6]
ruin_probability = []

def simulate_game(start_bankroll, target_bankroll, win_probability):

    bankroll = start_bankroll

    while 0 < bankroll < target_bankroll:
        x = random.random()
        if x <= win_probability:
            bankroll += 1
        else:
            bankroll -= 1

    if bankroll == 0:
        return True
    return False

def estimate_ruin_probability(start_bankroll, target_bankroll, win_probability):

    loss_nr = 0

    for _ in range(NUM_SIMULATIONS):
        if simulate_game(start_bankroll, target_bankroll, win_probability):
            loss_nr += 1
    
    return loss_nr/NUM_SIMULATIONS

###########     EXPERIMENT 1     ###########

for p in win_probabilities:
    ruin_probability.append(estimate_ruin_probability(10, 20, p))

plt.plot(win_probabilities, ruin_probability, marker="o")
plt.xlabel("Win Probability")
plt.ylabel("Probability of Ruin")
plt.title("Gambler's Ruin: Effect of Win Probability")
plt.grid(True)

output_dir = Path(__file__).resolve().parent.parent / "output"
output_dir.mkdir(parents=True, exist_ok=True)

plt.savefig(output_dir / "ruin_probability.png")
plt.close()

###########     EXPERIMENT 2     ###########

ruin_probability.clear()
for b in start_bankrolls:
    ruin_probability.append(estimate_ruin_probability(b, b * 2, 0.55))

plt.plot(start_bankrolls, ruin_probability, marker="o")
plt.xlabel("Starting Bankroll")
plt.ylabel("Probability of Ruin")
plt.title("Gambler's Ruin: Effect of Starting Bankroll")
plt.grid(True)

output_dir = Path(__file__).resolve().parent.parent / "output"
output_dir.mkdir(parents=True, exist_ok=True)

plt.savefig(output_dir / "bankroll_vs_ruin.png")
plt.close()