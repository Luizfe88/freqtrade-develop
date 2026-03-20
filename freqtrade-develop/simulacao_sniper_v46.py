# Simulação Quantitativa Sniper v4.6 - Expectancy, Profit Factor e PNL Projetado
# Baseado nos dados reais da v4.5 para escala exata do Freqtrade (stake + capital)

TARGET = 0.025      # 2.5% (minimal_roi)
STOP = -0.015       # -1.5% (stoploss)
NUM_TRADES = 246    # mesmo volume da v4.5
PREV_AVG_PCT = -0.06
PREV_TOTAL_PCT = -0.76
MULTIPLIER = abs(PREV_TOTAL_PCT / PREV_AVG_PCT)  # ~12.6667 - fator de escala stake/capital

def calcular_metricas(win_rate):
    expectancy = (win_rate * TARGET) + ((1 - win_rate) * STOP)
    avg_profit_pct = expectancy * 100
    wins = int(NUM_TRADES * win_rate)
    losses = NUM_TRADES - wins
    gross_profit = wins * TARGET
    gross_loss = losses * abs(STOP)
    profit_factor = gross_profit / gross_loss if gross_loss > 0 else float('inf')
    projected_total_pct = MULTIPLIER * avg_profit_pct
    return expectancy, profit_factor, avg_profit_pct, projected_total_pct, wins, losses

# Cálculo principal com win_rate 40%
win_rate_base = 0.40
exp, pf, avg_pct, total_pct, w, l = calcular_metricas(win_rate_base)

print("=== SIMULAÇÃO SNIPER v4.6 (Hack de Assimetria + 120min) ===")
print(f"Win Rate assumido: {win_rate_base*100:.2f}%")
print(f"Expectancy por trade: {exp*100:+.3f}%")
print(f"Avg Profit projetado: {avg_pct:+.3f}%")
print(f"Profit Factor: {pf:.3f}")
print(f"Trades simulados: {NUM_TRADES} ({w} vitórias / {l} perdas)")
print(f"PNL Total Projetado: {total_pct:+.2f}%  (escala real Freqtrade)")
print(f"Break-even teórico: {abs(STOP)/(TARGET + abs(STOP))*100:.1f}%")
print("\n=== TABELA DE SENSIBILIDADE (Win Rate) ===")
print("Win Rate | Expectancy | Avg Profit | Profit Factor | PNL Total Projetado")
for wr in [0.37, 0.38, 0.39, 0.40, 0.41, 0.42, 0.43, 0.44, 0.45]:
    e, p, a, t, _, _ = calcular_metricas(wr)
    print(f"{wr*100:5.1f}%   | {e*100:+6.3f}%   | {a:+6.3f}%   | {p:8.3f}      | {t:+7.2f}%")