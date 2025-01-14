import pytest
from datetime import datetime
from pybacktestchain.broker import Backtest_simple
from pybacktestchain.data_module import MomentumStrategy
from pybacktestchain.metrics import PortfolioMetrics
from datetime import datetime

def test_backtest_with_metrics():
    backtest = Backtest_simple(
        initial_date=datetime(2019, 1, 1),
        final_date=datetime(2020, 1, 1),
        information_class=MomentumStrategy,
        initial_cash=1000000,
        verbose=True
    )
    backtest.run_backtest()


    # Check if daily portfolio values are recorded 
    assert len(backtest.daily_portfolio_values) > 0, "Daily portfolio values were not recorded."

    # Check if the performance metrics are valid
    metrics = PortfolioMetrics(backtest.daily_portfolio_values)
    assert metrics.annualized_returns() is not None, "Annualized returns calculation failed."
    assert metrics.volatility() is not None, "Volatility calculation failed."
    assert metrics.sharpe_ratio() is not None, "Sharpe ratio calculation failed."
    assert metrics.max_drawdown() is not None, "Max drawdown calculation failed."