import sqlite3
import pandas as pd
from datetime import datetime

db_path = 'tradesv3.dryrun.sqlite'

def analyze_trades():
    try:
        conn = sqlite3.connect(db_path)
        # Selecionar trades fechados
        query = """
        SELECT 
            id, 
            pair, 
            open_date, 
            close_date, 
            close_profit, 
            close_profit_abs, 
            stake_amount, 
            exit_reason,
            leverage,
            is_short
        FROM trades 
        WHERE is_open = 0;
        """
        df = pd.read_sql_query(query, conn)
        conn.close()

        if df.empty:
            print("Nenhum trade fechado encontrado no banco de dados.")
            return

        # Converter datas
        df['open_date'] = pd.to_datetime(df['open_date'])
        df['close_date'] = pd.to_datetime(df['close_date'])

        # Cálculos
        total_pnl_abs = df['close_profit_abs'].sum()
        total_pnl_pct = df['close_profit'].mean() * 100 # Média dos lucros em %
        num_trades = len(df)
        wins = len(df[df['close_profit'] > 0])
        losses = len(df[df['close_profit'] <= 0])
        win_rate = (wins / num_trades) * 100 if num_trades > 0 else 0

        print("\n--- RESUMO DE TRADES FECHADOS ---")
        print(f"Total de Trades: {num_trades}")
        print(f"Vitórias: {wins}")
        print(f"Derrotas: {losses}")
        print(f"Win Rate: {win_rate:.2f}%")
        print(f"PNL Total (Absoluto): {total_pnl_abs:.8f}")
        print(f"Lucro Médio por Trade (%): {total_pnl_pct:.2f}%")
        
        print("\n--- DETALHES POR PAR ---")
        pair_stats = df.groupby('pair').agg({
            'close_profit_abs': 'sum',
            'close_profit': 'mean',
            'id': 'count'
        }).rename(columns={'id': 'trades'}).sort_values('close_profit_abs', ascending=False)
        print(pair_stats.to_string())
        
        print("\n--- ÚLTIMOS 5 TRADES ---")
        cols = ['pair', 'close_date', 'close_profit', 'close_profit_abs', 'exit_reason']
        print(df.sort_values('close_date', ascending=False).head(5)[cols].to_string(index=False))

    except Exception as e:
        print(f"Erro ao analisar trades: {e}")

if __name__ == "__main__":
    analyze_trades()
