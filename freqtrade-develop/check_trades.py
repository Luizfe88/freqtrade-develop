import sqlite3
import os

db_path = 'tradesv3.dryrun.sqlite'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, pair, open_date, open_rate, is_open, strategy FROM trades WHERE is_open=1;")
    rows = cursor.fetchall()
    print("Open Trades:")
    for row in rows:
        print(row)
    conn.close()
else:
    print("Database not found")
