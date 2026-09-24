## Projects

This repository contains a sequence of small, simulation-based projects designed
to build intuition for probability, expected value, risk, and market microstructure.

1. **Monte Carlo Expected Value**  

## Goal

This project explores how a positive expected-value strategy can still appear unprofitable over a limited number of trades.
The main idea is that positive expected value does not guarantee positive short-term P&L.

## Setup

Two games are compared.

Game A:
- 55% chance of winning +1
- 45% chance of losing -1
- Expected value = +0.10 per trade

Game B:
- 10% chance of winning +10
- 90% chance of losing -1
- Expected value = +0.10 per trade

Both games have the same expected value, but Game B has much higher variance.

## Experiment

For each horizon:

10, 20, 50, 100, 500, 1000 trades

the program runs 1000 independent simulations.

For each simulation, it calculates the final P&L and checks whether it is negative.

This estimates the probability that a positive-EV strategy is still unprofitable after a given number of trades.

The program also generates one cumulative P&L path for each game to show how the two strategies can behave differently over time.

## Results

Game A becomes unlikely to remain unprofitable relatively quickly.

Game B remains unprofitable much more often, even though both games have the same expected value.

The sample P&L paths also show that Game A tends to move more smoothly, while Game B experiences longer losing periods and larger jumps.

The generated plots are available in the `output` folder.

## Main Insight

Two strategies can have the same expected value but behave very differently in practice.

A high-variance positive-EV strategy can remain unprofitable for a long time before its edge becomes visible.

Expected value alone is therefore not enough to understand the short-term risk of a trading strategy.

## How to Run

Install the dependency:

pip install -r requirements.txt

Run the simulation:

python3 src/simulate.py

2. **Gambler’s Ruin**  
   Studies the probability of bankruptcy versus growth under finite bankroll constraints,
   even when the expected value is positive.

3. **Kelly Criterion**  
   Explores optimal bet sizing by simulating bankroll growth under different fractions,
   highlighting the trade-off between growth and drawdowns.

4. **Market Maker v0 (Fixed Spread)**  
   Simulates a basic market maker quoting a fixed spread and tracks inventory and P&L.

5. **Market Maker v1 (Adaptive Spreads)**  
   Extends the basic market maker by adjusting spreads based on inventory to manage risk.

6. **Poisson Order Flow**  
   Models order arrivals as a Poisson process and studies how arrival intensity affects
   inventory risk and P&L volatility.

7. **Volatility-Based Quoting**  
   Introduces stochastic price movement and studies how volatility impacts optimal spreads.

8. **Market Making Dashboard**  
   Integrates previous models into a single interactive environment to visualize inventory,
   P&L, and risk in real time.
