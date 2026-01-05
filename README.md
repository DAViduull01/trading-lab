## Projects

This repository contains a sequence of small, simulation-based projects designed
to build intuition for probability, expected value, risk, and market microstructure.

1. **Monte Carlo Expected Value**  
   Simulates simple betting strategies to show how positive-EV strategies can appear
   unprofitable over short horizons due to variance.

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
