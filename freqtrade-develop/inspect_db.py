import sqlite3

db_path = 'tradesv3.dryrun.sqlite'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(trades);")
columns = cursor.fetchall()
for col in columns:
    print(col)
conn.close()
