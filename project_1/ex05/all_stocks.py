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
    a = s[1].replace(" ", "").split(',')
    if '' in a:
        return
    for i in range(len(a)):
        c = 0
        if a[i].upper() not in STOCKS:
            c += 1
        else:
            b = STOCKS[a[i].upper()]
            for k, v in COMPANIES.items():
                if v == a[i].upper():
                    print(f"{v} is a ticker symbol for {k}")
                    break

        if a[i].title() not in COMPANIES:
            c += 1
        else:
            b = COMPANIES[a[i].title()]
            print(f"{a[i].title()} stock price is {STOCKS[b]}")

        if c == 2:
            print(f'{a[i]} is an unknown company or an unknown ticker symbol')
    
def main():
    if len(sys.argv) == 2:
        keys()
    return

if __name__ == '__main__':
    main()
