import pytest
from pybacktestchain.data_module import MeanReversionStrategy  
from pybacktestchain.broker import Backtest_simple
from datetime import datetime

def test_meanreversion_strategy():  
    # Set verbosity for logging
    verbose = True  # Enable logging output during the test

    # Initialize the backtest
    backtest = Backtest_simple(
        initial_date=datetime(2019, 1, 1),
        final_date=datetime(2019, 3, 1),
        information_class=MeanReversionStrategy,
        initial_cash=1000000,
        verbose=verbose
    )

    # Run the backtest
    backtest.run_backtest()

    # Assert that the backtest ran successfully
    transaction_log = backtest.broker.get_transaction_log()
    assert not transaction_log.empty, "No transactions recorded in the backtest!"