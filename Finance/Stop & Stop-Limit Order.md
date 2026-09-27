---
tags:
  - "finance"
---

Stop and stop-limit orders are instructions to buy or sell once a stock reaches a trigger price, the **stop price**. They are commonly used to limit losses or protect gains without watching the market continuously.[^orders]

## Order Types

- **Stop order (stop-loss).** When the stop price is reached, it becomes a **market order** and executes at the next available price. Execution is almost certain, but the price is not guaranteed and can be well below the stop in a fast market or after a gap.[^orders]
- **Stop-limit order.** When the stop price is reached, it becomes a **limit order** that executes only at the limit price or better. The price is protected, but the order may not execute at all.[^orders]
- **Trailing stop.** The stop price is set a fixed amount or percentage from the market price and moves as the price moves in the investor's favour, but never back.[^orders]

Trading venues differ on whether the last trade or the quoted price triggers a stop, so check the broker's rules.[^orders]

## Worked Example: Stop-Limit Sell

**Inputs:** a sell stop-limit order with a stop price of $3.00 and a limit price of $2.50 (the Investor.gov example).[^orders]

**Step 1: trigger.** The price falls to $3.00, and the order becomes a limit order to sell at $2.50 or better.

**Step 2: outcome.** If the price keeps falling below $2.50 before the order fills, it does not execute and the investor still holds the shares. A plain stop order would have sold, at whatever price was available.

## Worked Example: Trailing Stop

**Inputs:** shares bought at $20, now at $22, with a trailing stop set $1 below the market price.[^orders]

**Step 1: initial stop.**

$$
22 - 1 = 21
$$

**Step 2: price peaks at $24.**

$$
24 - 1 = 23
$$

**Step 3: price falls back.** The stop stays at $23; if the price reaches it, the order becomes a market order to sell.

The trailing stop locked in most of the gain from $20 to $24 while letting the position ride upwards.

## Related Notes

- [[Technical Indicators]] — traders often place stops around technical levels.

## References & Useful Links

[^orders]: [Investor.gov, "Investor Bulletin: Understanding Order Types"](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14) — Stop, stop-limit and trailing stop orders, the $3.00 / $2.50 stop-limit example, the $20 → $24 trailing-stop example, and trigger differences between venues.
