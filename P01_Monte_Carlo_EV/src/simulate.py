import random
import matplotlib.pyplot as plt

random.seed(42)

NUM_SIMULATIONS = 1000
PATH_LENGTH = 1000
HORIZONS = [10, 20, 50, 100, 500, 1000]

###########     HELPER FUNCTIONS     ###########

def simulate_losing_probability(win_probability, win_payoff, loss_amount, n):

    losing_simulations = 0

    for _ in range(NUM_SIMULATIONS):
        total_pnl = 0

        for _ in range(n):
            x = random.random()

            if x < win_probability:
                total_pnl += win_payoff
            else: 
                total_pnl -= loss_amount

        if total_pnl < 0:
            losing_simulations += 1
    
    return losing_simulations / NUM_SIMULATIONS

def simulate_pnl_path(win_probability, win_payoff, loss_amount, n):

    total_pnl = 0
    pnl_path = []

    for _ in range(n):
        x = random.random()

        if x < win_probability:
            total_pnl += win_payoff
        else:
            total_pnl -= loss_amount
        pnl_path.append(total_pnl)

    return pnl_path


###########     GAME A     ###########

print("Game A: 0.55 * 1 + 0.45 * (-1)")

game_a_losing = []

for n in HORIZONS:

    losing_probability = simulate_losing_probability(0.55, 1, 1, n)
    game_a_losing.append(losing_probability)

    print(n, losing_probability)

###########     GAME B     ###########

game_b_losing = []

print("\n")
print("Game B: 0.1 * 10 + 0.9 * (-1)")

for n in HORIZONS:

    losing_probability = simulate_losing_probability(0.1, 10, 1, n)
    game_b_losing.append(losing_probability)

    print(n, losing_probability)

###########     LOSING PROBABILITY PLOT     ###########

plt.plot(HORIZONS, game_a_losing, marker="o", label="Game A")
plt.plot(HORIZONS, game_b_losing, marker="o", label="Game B")

plt.xlabel("Number of trades")
plt.ylabel("Probability of negative P&L")
plt.title("Positive EV Can Look Unprofitable")
plt.legend()
plt.grid()

plt.savefig("../output/losing_probability.png")
plt.close()

###########     PROFIT AND LOSS PLOT     ###########

pnl_path_a = simulate_pnl_path(0.55, 1, 1, PATH_LENGTH)  # GAME A

pnl_path_b = simulate_pnl_path(0.1, 10, 1, PATH_LENGTH)  # GAME B


plt.plot(pnl_path_a, label="Game A")
plt.plot(pnl_path_b, label="Game B")

plt.axhline(0)
plt.xlabel("Trade")
plt.ylabel("Cumulative P&L")
plt.title("Sample P&L Paths")
plt.legend()
plt.grid()

plt.savefig("../output/sample_pnl_paths.png")
plt.close()