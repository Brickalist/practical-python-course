# report.py
#
# Exercise 2.4

import csv

'''list[(shareName, numberOfOwnedShares, sharePrice)]'''
type portfolioContainer = list[tuple[str, int, float]]
'''list[{shareName, bumberOfOwnedShares, sharePrice}]'''
type portfolioDict = list[dict[str, str | int | float]]
'''dict{shareName, price}'''
type priceDict = dict[str, float]

def read_portfolio_tuple(filename: str) -> portfolioContainer | None:
    '''Reads a csv of share names, number of shares and prices and returns a tuple'''

    portfolio: portfolioContainer = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # Skip the first row since it contains the table names instead of data
        next(rows)
        for row in rows:
            if len(row) == 3:
                portfolio.append((row[0], int(row[1]), float(row[2])))
            else:
                print(f'Bad data: {row}')


    return portfolio

def read_portfolio_dict(filename: str) -> portfolioDict | None:
    '''Reads a csv of share names, number of shares and prices and returns a dictonary'''

    portfolio: portfolioDict = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # Skip the first row since it contains the table names instead of data 
        next(rows)
        for row in rows:
            if len(row) == 3:
                portfolio.append({'name': row[0], 'shares': int(row[1]), 'price': float(row[2])})
            else:
                print(f'Bad data: {row}')

    return portfolio

def read_prices(filename: str) -> priceDict | None:
    '''Reads a csv of share names and current prices and returns a dictionary'''

    prices: priceDict = {} 
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                prices[row[0]] = float(row[1])
            else:
                print(f'Bad data: {row}')

    return prices

pf = read_portfolio_tuple("Data/portfolio.csv")
pfd = read_portfolio_dict("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

buyValue: float = 0
currentValue: float = 0
gain: float = 0
if pf and prices:
    for name, shares, price in pf:
        buyValue += price
        currentPrice = prices.get(name)
        if currentPrice:
            currentValue += currentPrice

gain = (currentValue - buyValue) / buyValue * 100
print(f'Initial portfolio value: {buyValue:.2f}. Current portfolio value: {currentValue:.2f}. Gain: {gain:.2f}%')


