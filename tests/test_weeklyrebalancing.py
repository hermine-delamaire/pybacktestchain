from datetime import datetime, timedelta
from pybacktestchain.broker import EndOfWeek

# Test dates
start_date = datetime(2023, 1, 1)  # Sunday
end_date = datetime(2023, 1, 31)  # End of January
dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Weekly Rebalance
weekly_rebalance = EndOfWeek()
print("Weekly Rebalance (End of Week):")
for date in dates:
    print(f"{date.date()}: {weekly_rebalance.time_to_rebalance(date)}")
