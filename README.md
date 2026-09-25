# Stock Strategy Backtester (A Level NEA)

A Python desktop app that backtests simple investment strategies on historical daily stock prices and compares each result with a 3% savings rate. Built for my A Level Computer Science NEA (graded A*).

## What it does

* Loads daily open, high, low and close prices from a CSV file.
* Lets you choose one or more strategies in a Tkinter settings window and set the backtest length in years.
* Invests a fixed £100,000 over the chosen period, then reports the final number of shares, their value at the last price, the percentage return, and what 3% annual interest would have earned over the same period.

## Strategies

* **Buy and hold:** splits the money into equal yearly lump sums, one every 252 trading days.
* **Dollar cost averaging (DCA):** splits the money into equal weekly purchases.
* **Trend trading:** calculates a 90 day simple moving average (SMA) and a 30 day exponential moving average (EMA), uses EMA minus SMA as a trend strength signal, and finds the crossover points where that signal changes sign. The aim is to invest only while the trend is up. Work in progress (see Status).

## Example output

On the default dataset (`IUCS.L.csv`, 1,736 trading days from March 2017 to February 2024), the program reports:

* Buy and hold: £143,319 (+43.3%)
* DCA: £135,795 (+35.8%)
* 3% interest over the same period: +23.0%

## Design

The code is object oriented. A single `Program` object owns `StockData`, `Simulation` and `UI`, and each of those keeps a reference back to `Program` so they can reach each other.

Every strategy inherits from `IStrategy` and overrides `_PerformStrategy()`. `Simulation` keeps a list of active strategies and runs them all through one loop, so it never needs to know which strategy it is running. Adding a new strategy means writing one subclass and adding one checkbox.

## Project structure

```
nea/
  Program.py          Entry point. Creates StockData, Simulation and UI
  UI.py               Tkinter settings window (strategy checkboxes, time period, Test button)
  StockData.py        Parses a CSV into [date, open, high, low, close] rows, oldest first
  Simulation.py       Holds the active strategies and runs them
  IStrategy.py        Base class for all strategies
  BuyAndHold.py       Buy and hold strategy
  DCA.py              Dollar cost averaging strategy
  TrendTrading.py     SMA/EMA crossover strategy
  StrategyUtil.py     SMA, EMA and trend strength calculations
  Graph.py            Tkinter canvas chart: price (green), SMA (blue), EMA (red), strength (purple)
  GraphUtil.py        Scaling and normalisation for the chart
  object_stuff.py     Early sketch of the class design
  *.csv, *.xlsx       Sample price data
```

## Running it

You need Python 3.9 or later with Tkinter (included in the standard python.org installers). There are no third party packages.

```
git clone https://github.com/sebhoving/NEA-A-Level.git
cd NEA-A-Level/nea
python Program.py
```

Run it from inside `nea/`, because the data file paths are relative.

In the window:

1. To change the backtest length, enter a number of years and click **Amend Time Period**. This resets the window, so do it first. The default is the whole dataset.
2. Tick the strategies you want to compare.
3. Click **Test**. Results print to the terminal.

## Using your own data

Change the file name in `Program.py`. The CSV needs a header row `Date,Open,High,Low,Close`, dates in DD/MM/YYYY format and rows ordered oldest first, as in `IUCS.L.csv`. The DJIA file (US date format, newest first) is handled as a special case. The other sample files do not load as they are.

## Status

* Trend trading finds the crossover points, but its trading rule is unfinished. On the default data it stops with an index error and does not report a final value.
* The chart in `Graph.py` is not opened by `Program.py` at the moment (the line is commented out).
* The data frequency setting is stored but not yet used by the strategies.
* Results print to the terminal rather than the window.
