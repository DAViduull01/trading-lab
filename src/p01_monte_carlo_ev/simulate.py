import numpy as np
import matplotlib.pyplot as plt


def looks_losing_after_n_trials(
    n_trials: int,
    n_check: int,
    win_payoff: float,
    lose_payoff: float,
    p_win: float,
    n_runs: int = 1000,
):
    losing_count = 0

    for seed in range(n_runs):
        cum_avg = simulate_game(
            n_trials,
            win_payoff,
            lose_payoff,
            p_win,
            seed=seed,
        )

        if cum_avg[n_check - 1] < 0:
            losing_count += 1

    return losing_count / n_runs


def simulate_game(n, win_payoff, lose_payoff, p_win, seed):
    rng = np.random.default_rng(seed)
    wins = rng.random(n) < p_win
    outcomes = np.where(wins, win_payoff, lose_payoff).astype(float)
    cum_sum = np.cumsum(outcomes)
    cum_avg = cum_sum / np.arange(1, n + 1)
    return cum_avg


def main():
    N = 1_000_000

    games = [
        ("A: Fair coin (+1/-1, p=0.5)", 1, -1, 0.50, 1),
        ("B: Slight edge (+1/-1, p=0.51)", 1, -1, 0.51, 2),
        ("C: Asymmetric (+10/-1, p=0.1)", 10, -1, 0.10, 3),
    ]

    '''for title, w, l, p, seed in games:
        cum_avg = simulate_game(N, w, l, p, seed)
        true_ev = p * w + (1 - p) * l

        plt.figure(figsize=(12, 6))
        plt.plot(cum_avg, linewidth=2)
        plt.axhline(true_ev, linestyle="--", linewidth=1)
        plt.title(f"{title} | True EV = {true_ev:.3f}")
        plt.xlabel("Trials")
        plt.ylabel("Cumulative average payoff")
        plt.xlim(0, 1000)
        plt.tight_layout()
        plt.savefig(f"outputs/{title.split(':')[0]}.png")


    plt.show()'''

    print("\nProbability strategy looks losing after N trades:\n")

    check_points = [10, 20, 50, 100, 200, 500, 1000]
    games_to_test = [
        ("A: Fair coin", 1, -1, 0.50),
        ("B: Slight edge", 1, -1, 0.51),
        ("C: Asymmetric", 10, -1, 0.10),
    ]

    n_runs = 5000  # reduce Monte Carlo noise
    max_check = max(check_points)

    for name, w, l, p in games_to_test:
        print(name)
        for n_check in check_points:
            prob_losing = looks_losing_after_n_trials(
                n_trials=max_check,   # IMPORTANT: just enough
                n_check=n_check,
                win_payoff=w,
                lose_payoff=l,
                p_win=p,
                n_runs=n_runs,
            )
            print(f"  after {n_check:>4}: {prob_losing:6.2%}")
        print()



if __name__ == "__main__":
    main()
