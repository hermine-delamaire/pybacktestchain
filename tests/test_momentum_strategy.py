import pytest
from pybacktestchain.data_module import MomentumStrategy  # Adjust if the class is MomentumStrategy
from pybacktestchain.broker import Backtest_simple
from datetime import datetime

def test_momentum_strategy():  
    # Set verbosity for logging
    verbose = True  # Enable logging output during the test

    # Initialize the backtest
    backtest = Backtest_simple(
        initial_date=datetime(2019, 1, 1),
        final_date=datetime(2019, 3, 1),
        information_class=MomentumStrategy,
        initial_cash=1000000,
        verbose=verbose
    )

    # Run the backtest
    backtest.run_backtest()

    # Assert that the backtest ran successfully (for example, check the transaction log exists)
    transaction_log = backtest.broker.get_transaction_log()
    assert not transaction_log.empty, "No transactions recorded in the backtest!"