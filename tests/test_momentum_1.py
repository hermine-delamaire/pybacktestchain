from datetime import datetime
import pandas as pd
from pybacktestchain.data_module import MomentumStrategy, DataModule

# Create mock data
data = pd.DataFrame({
    'Date': pd.date_range(start='2022-01-01', periods=10).tolist() * 3,
    'ticker': ['AAPL'] * 10 + ['MSFT'] * 10 + ['GOOGL'] * 10,
    'Adj Close': [150, 152, 154, 153, 155, 157, 160, 162, 164, 165] +
                 [300, 302, 304, 306, 308, 310, 312, 314, 316, 318] +
                 [2800, 2810, 2820, 2830, 2840, 2850, 2860, 2870, 2880, 2890]
})

# Initialize DataModule
data_module = DataModule(data=data)

# Initialize MomentumStrategy
momentum_strategy = MomentumStrategy(data_module=data_module, look_back_period=5)

# Test compute_portfolio
test_date = datetime(2022, 1, 10)
portfolio_weights = momentum_strategy.compute_portfolio(test_date, None)

print(f"Portfolio weights on {test_date}: {portfolio_weights}")
