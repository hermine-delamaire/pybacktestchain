from datetime import datetime, timedelta
from pybacktestchain.broker import EndOfDay

# Test dates
start_date = datetime(2023, 1, 1)  # Start on a Sunday
end_date = datetime(2023, 1, 7)  # End on the next Saturday
dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Daily Rebalance
daily_rebalance = EndOfDay()
print("Daily Rebalance:")
for date in dates:
    print(f"{date.date()}: {daily_rebalance.time_to_rebalance(date)}")
