The measure is computed by calculating the returns the investment has made in excess of the risk free rate.

### Sharpe Implementation

```python
import numpy as np  
close_prices = [...]# logarithmic returns using the closing price   
returns = np.log(close_prices / close_prices.shift(1))  
volatility = returns.std() * np.sqrt(252)   
sharpe_ratio = (returns.mean() - 0.05) / volatility
```