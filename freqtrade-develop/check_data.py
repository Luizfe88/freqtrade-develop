
import pandas as pd
import json
import os

data_path = "user_data/data/binance/BTC_USDT-1d.json"

if os.path.exists(data_path):
    print(f"File found: {data_path}")
    with open(data_path, 'r') as f:
        data = json.load(f)
        df = pd.DataFrame(data, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
        print(f"Rows: {len(df)}")
        print(f"Last date: {df.iloc[-1]['date']}")
        # Convert date
        df['date'] = pd.to_datetime(df['date'], unit='ms')
        print(f"Converted Last date: {df.iloc[-1]['date']}")
else:
    print(f"File NOT found: {data_path}")
    # Check directory
    dir_path = "user_data/data/binance/"
    if os.path.exists(dir_path):
        print(f"Files in {dir_path}: {os.listdir(dir_path)}")
