# Project 1 — Monte Carlo Expected Value

## Goal
Understand how expected value emerges over time and why short-term outcomes
can be misleading even for positive-EV strategies.

## Setup
I simulated three betting games:
- A fair coin (EV = 0)
- A small-edge strategy (p = 0.51)
- An asymmetric payoff strategy (+10 with p = 0.1)

## Experiment
For each strategy, I ran repeated simulations and measured how often the
cumulative average payoff was negative after N trades (N = 10, 20, 50, 100, …).

## Key Results
- Even positive-EV strategies frequently appear losing after short horizons.
- The asymmetric strategy, despite having the highest EV, looked losing almost
  45% of the time after 100 trades.
- As the evaluation horizon increases, the probability of looking losing decreases,
  but convergence is slow.

## Trading Insight
Expected value is not observable in the short run.
Traders must reason in terms of distributions, variance, and appropriate
evaluation horizons rather than short-term P&L.

## Explanation 
I simulated several betting strategies to study how often positive-EV strategies
appear unprofitable in short samples. I found that variance dominates early outcomes,
especially for asymmetric payoffs, causing good strategies to look bad for long periods.
This explains why traders evaluate strategies over long horizons and focus on risk
and distributional properties rather than short-term results.
