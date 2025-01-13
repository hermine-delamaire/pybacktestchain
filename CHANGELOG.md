# CHANGELOG

## v0.6.0 (2025-01-13)

### Added

- Created EndOfDay and EndOfWeek class for daily and weekly rebalancing
- Enhanced CLI to support:
    - multiple strategies via "--strategies"
    - dynamic rebalancing frequency via "--rebalance-frequency"

### Fixed

- Minor bugs for CLI arguments handling

### Changed 

- Updated CLI to use "--strategies" instead of "--strategy" 
- Adjusted the rebalancing logic to be more flexible and dyanamic for the user

## v0.5.0 (2025-01-13)

### Added

- Support for custom universe with the "--universe" argument in the CLI file. With a CSV file, users can specify their own universe.
- Created a custom_universe file to test this new feature 

### Fixed

- Checked that the CSV file contained a ticker column to move forward


## v0.4.0 (2025-01-13)

### Added

- Added a MeanReversionStrategy class (to target underpriced assets based on historical average, tendency to revert to historical mean)
- Added an EqualWeightsStrategy class (to allocated ewqual weights to all assets constituting the portfolio)
- Updated CLI to include these new strategies

### Fixed

- Tried to implement a backtest for both new strategies

## v0.3.0 (2025-01-13)

### Added 

- Added Command Line Interface functionality for Backtest_simple and Backtest classes
- Integrated support for two strategies (Momentum and FirstTwoMoments)

### Fixed 

- Adressed execution issues with cli.py (had forgotted to call main at the end)


## v0.2.0 (2025-01-12)

### New Class Added 

Backtest_simple class for testing momentum strategy.
- Failed to run the test


## v0.1.0 (2025-01-12)

### Added

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
