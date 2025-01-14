# CHANGELOG

## v0.7.3 (2025-01-14)

### Change

- Changed name project and author

## v0.7.2 (2025-01-14)

### Add

- Specified Know Issues in the README file

## v0.7.1 (2025-01-14)

### Add

- Added additional information and details in the README file for better understanding

## v0.7.0 (2025-01-14)

### Add

- Created PortfolioMetrics class to calculate advanced performance metrics including:
    - Annualized Return
    - Volatility
    - Sharpe Ratio
    - Max Drawdown
- Integrated these metrics into Backtest_simple class
- Added a unit test for these metrics test_backtest_metrics

### Fix

- Fixed naming issues with lack of consistency across the code 'annualized_return' vs 'annualized_returns'

## v0.6.0 (2025-01-13)

### Add

- Created EndOfDay and EndOfWeek class for daily and weekly rebalancing
- Enhanced CLI to support:
    - multiple strategies via "--strategies"
    - dynamic rebalancing frequency via "--rebalance-frequency"

### Fix

- Minor bugs for CLI arguments handling

### Change

- Updated CLI to use "--strategies" instead of "--strategy" 
- Adjusted the rebalancing logic to be more flexible and dyanamic for the user

## v0.5.0 (2025-01-13)

### Add

- Support for custom universe with the "--universe" argument in the CLI file. With a CSV file, users can specify their own universe.
- Created a custom_universe file to test this new feature 

### Fix

- Checked that the CSV file contained a ticker column to move forward

## v0.4.0 (2025-01-13)

### Add

- Added a MeanReversionStrategy class (to target underpriced assets based on historical average, tendency to revert to historical mean)
- Added an EqualWeightsStrategy class (to allocated ewqual weights to all assets constituting the portfolio)
- Updated CLI to include these new strategies

### Fix

- Tried to implement a backtest for both new strategies

## v0.3.0 (2025-01-13)

### Add

- Added Command Line Interface functionality for Backtest_simple and Backtest classes
- Integrated support for two strategies (Momentum and FirstTwoMoments)

### Fix

- Adressed execution issues with cli.py (had forgotted to call main at the end)

## v0.2.0 (2025-01-12)

### Add 

Backtest_simple class for testing momentum strategy.
- Failed to run the test

## v0.1.0 (2025-01-12)

### Add

Momentumstrategy` class for implementing a momentum strategy.
- Computes portfolio weights based on past returns.
- Designed with a look-back period which can be adjusted.
- Takes care of special cases including missing or negative returns.

## v0.0.1 (2024-08-28)

### Fix

* fix: Prepare for first branch ([`63be4e0`](https://github.com/jfimbett/pybacktestchain/commit/63be4e072a5a4816a54cfe573d4a119e96f8f872))

* fix: setup ([`bc3e658`](https://github.com/jfimbett/pybacktestchain/commit/bc3e658013653d5d9e9249fde2bfccec4799eba1))

### Unknown

* First commit ([`580ef4d`](https://github.com/jfimbett/pybacktestchain/commit/580ef4d049d1646b8122efe24d57f7567aa89bd8))
