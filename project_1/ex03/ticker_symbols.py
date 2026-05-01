import sys

def keys():
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
    elif s[1].upper() not in STOCKS:
        print('Unknown ticker')
    else:
        b = STOCKS[s[1].upper()]
        for k, v in COMPANIES.items():
            if v == s[1].upper():
                print(k, b)
                break

if __name__ == "__main__":
    keys()
