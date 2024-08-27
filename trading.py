import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import backtrader as bt

# 1. Téléchargement des données historiques directement dans Backtrader
class SMACross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=50), bt.ind.SMA(period=200)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

# 2. Configuration du moteur de backtesting
cerebro = bt.Cerebro()
cerebro.addstrategy(SMACross)

# 3. Téléchargement des données via yfinance et conversion pour Backtrader
data = bt.feeds.PandasData(dataname=yf.download("AAPL", start="2018-01-01", end="2023-01-01"))

# 4. Ajout des données au moteur de backtesting
cerebro.adddata(data)

# 5. Configuration de l'investissement initial
cerebro.broker.setcash(100000)  # $100,000
cerebro.broker.setcommission(commission=0.001)

# 6. Lancer la simulation
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())

# 7. Affichage du graphique
cerebro.plot()
