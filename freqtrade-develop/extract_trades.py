import sqlite3
import pandas as pd
from datetime import datetime

db_path = 'tradesv3.dryrun.sqlite'
date_today = '2026-03-13'

conn = sqlite3.connect(db_path)
query = f"SELECT pair, open_date, close_date, close_profit, exit_reason, is_open, max_rate, min_rate, open_rate FROM trades WHERE open_date >= '{date_today} 00:00:00';"
df = pd.read_sql_query(query, conn)
conn.close()

if df.empty:
    print("Nenhum trade encontrado para hoje.")
else:
    print(df.to_string())
