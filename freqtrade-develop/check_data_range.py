import pandas as pd
import os

path = r'c:\Users\luizf\Documents\polymarket\freqtrade-develop\freqtrade-develop\user_data\data\binance\BTC_USDT-5m.feather'
if os.path.exists(path):
    df = pd.read_feather(path)
    print(f"File: {path}")
    print(f"Total rows: {len(df)}")
    if len(df) > 0:
        print(f"First date: {df['date'].min()}")
        print(f"Last date: {df['date'].max()}")
else:
    print("File not found.")
