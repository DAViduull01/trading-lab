import random
from pathlib import Path
import matplotlib.pyplot as plt

random.seed(42)
WIN_PROBABILITY = 0.55
NUM_SIMULATIONS = 10000
START_BANKROLL = 40

output_dir = Path(__file__).resolve().parent.parent / "output"
output_dir.mkdir(parents=True, exist_ok=True)

start_bankrolls = [5, 10, 20, 30, 50]
win_probabilities = [0.5, 0.51, 0.55, 0.6]
bet_sizes = []

win_ruin_probabilities = []
bankroll_ruin_probabilities = []
bet_ruin_probabilities = []

def simulate_game(start_bankroll, target_bankroll, win_probability, bet_size):

    bankroll = start_bankroll

    while 0 < bankroll < target_bankroll:
        x = random.random()
        if x <= win_probability:
            bankroll += bet_size
        else:
            bankroll -= bet_size

    if bankroll <= 0:
        return True
    return False

def estimate_ruin_probability(start_bankroll, target_bankroll, win_probability, bet_size):

    loss_nr = 0

    for _ in range(NUM_SIMULATIONS):
        if simulate_game(start_bankroll, target_bankroll, win_probability, bet_size):
            loss_nr += 1
    
    return loss_nr / NUM_SIMULATIONS

def simulate_bankroll_path(start_bankroll, target_bankroll, win_probability):

    bankroll = start_bankroll
    path = [bankroll]

    while 0 < bankroll < target_bankroll:
        x = random.random()
        if x <= win_probability:
            bankroll += 1
        else:
            bankroll -= 1
        path.append(bankroll)

    return path

###########     EXPERIMENT 1: WIN PROBABILITY VS RUIN PROBABILITY     ###########

for p in win_probabilities:
    win_ruin_probabilities.append(100 * estimate_ruin_probability(10, 20, p, 1))

plt.plot(win_probabilities, win_ruin_probabilities, marker="o")
plt.xlabel("Win Probability")
plt.ylabel("Probability of Ruin %")
plt.title("Gambler's Ruin: Effect of Win Probability")
plt.grid(True)

plt.savefig(output_dir / "ruin_probability.png")
plt.close()

###########     EXPERIMENT 2: STARTING BANKROLL VS RUIN PROBABILITY     ###########

for b in start_bankrolls:
    bankroll_ruin_probabilities.append(100 * estimate_ruin_probability(b, b * 2, WIN_PROBABILITY, 1))

plt.plot(start_bankrolls, bankroll_ruin_probabilities, marker="o")
plt.xlabel("Starting Bankroll ($)")
plt.ylabel("Probability of Ruin %")
plt.title("Gambler's Ruin: Effect of Starting Bankroll")
plt.grid(True)

plt.savefig(output_dir / "bankroll_vs_ruin.png")
plt.close()

###########     EXPERIMENT 3: SAMPLE BANKROLL PATHS     ###########

for i in range(10):
    path = simulate_bankroll_path(10, 20, WIN_PROBABILITY)
    plt.plot(path, label=f"Game {i + 1}")

plt.xlabel("Number of Bets")
plt.ylabel("Bankroll ($)")
plt.title("Gambler's Ruin: Sample Bankroll Paths")
plt.legend()
plt.grid(True)

plt.savefig(output_dir / "sample_paths.png")
plt.close()

###########     EXPERIMENT 4: BET SIZE VS RUIN PROBABILITY     ###########

for bet in range(1, int(START_BANKROLL / 2) + 1):
        if START_BANKROLL % bet == 0:
            bet_sizes.append(bet)

for bet in bet_sizes:
    bet_ruin_probabilities.append(100 * estimate_ruin_probability(START_BANKROLL, START_BANKROLL * 2, WIN_PROBABILITY, bet))

plt.plot(bet_sizes, bet_ruin_probabilities, marker="o")

plt.xlabel("Bet Size ($)")
plt.ylabel("Probability of Ruin %")
plt.title("Gambler's Ruin: Effect of Bet Size")

plt.xticks(bet_sizes)
plt.grid(True)

plt.savefig(output_dir / "bet_size_vs_ruin.png")
plt.close()

