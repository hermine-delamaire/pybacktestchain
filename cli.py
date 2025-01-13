import argparse
from datetime import datetime
from pybacktestchain.broker import Backtest, Backtest_simple
from pybacktestchain.broker import EndOfMonth, StopLoss
from pybacktestchain.data_module import MomentumStrategy, Information, FirstTwoMoments, EqualWeightStrategy, MeanReversionStrategy

def main():
    # Setting up the arguments
    parser = argparse.ArgumentParser(description="Running backtests with pybacktestchain.")
    parser.add_argument("--start-date", required=True, type=str, help="This is the start date for the backtest (YYYY-MM-DD).")
    parser.add_argument("--end-date", required=True, type=str, help="This is the end date for the backtest (YYYY-MM-DD).")
    parser.add_argument("--initial-cash", type=int, default=1000000, help="This is the initial cash for the portfolio.")
    parser.add_argument("--verbose", action="store_true", help="Enable detailed logging.")
    # Simple backtest is the one I created, Advanced backtest is the one that we had in class already for the blockchain
    parser.add_argument("--mode", type=str, choices=["simple", "advanced"], default="simple", help="Select the backtest mode: simple or advanced.")
    parser.add_argument("--strategy", type=str, choices=["momentum", "first_two_moments", "mean_reversion", "equal_weight"], default="momentum", help="Select the strategy for the backtest.")
    parser.add_argument("--universe", type=str, help="Provide the path to a csv file containing the stock tickers.")

    args = parser.parse_args()

    # Creating a dictionnary with the different strategies available
    strategy_map = {
        "momentum": MomentumStrategy,
        "first_two_moments": FirstTwoMoments,
        "mean_reversion": MeanReversionStrategy,
        "equal_weight": EqualWeightStrategy,
    }

    strategy_class = strategy_map[args.strategy]

    # Load universe from CSV if specified as such
    if args.universe:
        import pandas as pd
        universe_df = pd.read_csv(args.universe)
        if 'ticker' not in universe_df.columns:
            raise ValueError("The custom universe file must contain a 'ticker' column.")
        universe = universe_df['ticker'].tolist()
        print(f"[INFO] Loaded custom universe: {universe}")
    else:
        universe = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'INTC', 'CSCO', 'NFLX']


    # Running the backtest in the mode chosen
    if args.mode == "simple":
        print("[INFO] Running simple backtest...")
        backtest = Backtest_simple(
            initial_date=datetime.strptime(args.start_date, "%Y-%m-%d"),
            final_date=datetime.strptime(args.end_date, "%Y-%m-%d"),
            information_class=strategy_class,
            initial_cash=args.initial_cash,
            verbose=args.verbose,
            universe=universe
        )

    else:
        print("[INFO] Running advanced backtest...")
        backtest = Backtest(
            initial_date=datetime.strptime(args.start_date, "%Y-%m-%d"),
            final_date=datetime.strptime(args.end_date, "%Y-%m-%d"),
            information_class=strategy_class,
            rebalance_flag=EndOfMonth,
            risk_model=StopLoss,
            initial_cash=args.initial_cash,
            verbose=args.verbose,
            universe=universe
        )

    backtest.run_backtest
    print("Backtest is now completed. Check the transaction log for details")

if __name__ == "__main__":
    main()