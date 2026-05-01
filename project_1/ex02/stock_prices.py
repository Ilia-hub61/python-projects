import sys

def dictionary():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    s = sys.argv
    if len(s) == 1 or len(s) > 2:
        pass
    elif s[1].title() not in COMPANIES:
        print('Unknown company')
    else:
        b = COMPANIES[s[1].title()]
        print(STOCKS[b])

if __name__ == '__main__':
    dictionary()
