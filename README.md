# Regression

The aim of the project is to allow the user to:

1. Download stock data.
2. Run a regression (Simple Linear) analysis on the stocks of your choice.
3. Visualise the output in a matplotlib chart.

### Python dependencies

1. mysql.connector
2. maplotlib.pyplot
3. numpy
4. scipy
5. pandas
6. yfinance

### Instructions

1. Create database named 'global' using dump.sql file
2. Populate database
3. Edit downloader.py line 23 time period argument to the amount of historical days of data you require. If you want the maximum amount of historical data replace `period = 4d` with `period = max`. For further documentation on the stoack data module, visit the Github page of  [Ran Aroussi](https://github.com/ranaroussi/yfinance)
4. Run ukequities.py
5. Command line outputs describe which asset pairs have a Standard Deviation larger than 2. This qualifier can be changed on line 31 "if sigma > 2"
