import pytest
import requests
from bs4 import BeautifulSoup
import re


def get_response(ticker):
    html_content = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Referer": "https://www.google.com/"
    }
    path = f"https://finance.yahoo.com/quote/{ticker}/financials/?p={ticker}"
    response = requests.get(path, headers=headers)
    if response.status_code == 200:
        html_content = response.text
        if "noData yf-wnifss" in html_content:
            raise Exception("Unknown ticker")
    else:
        raise requests.RequestException(f"Error HTTP request: {response.status_code}")
    return html_content


def parse_page(html, breakdown):
    soup = BeautifulSoup(html, "html.parser")
    breakdowns = soup.find_all("div", class_="row lv-0 yf-t22klz")
    breakdown_flag = 0
    res = []
    for item in breakdowns:
        title = item.find("div", class_="rowTitle yf-t22klz").text
        if title == breakdown:
            breakdown_flag = 1
            res.append(title)
            stats = item.find_all("div", class_=re.compile(r"column yf-t22klz( alt)?"))
            for stat in stats:
                res.append(stat.text.strip(" "))
            print(tuple(res))
            break
    if not breakdown_flag:
        raise Exception("Breakdown or ticker not found")
    return tuple(res)

def get_financials(ticker, field):
    html = get_response(ticker)
    return parse_page(html, field)

def test_total_revenue_msft():
    result = get_financials('MSFT', 'Total Revenue')
    assert isinstance(result, tuple)
    assert result[0] == 'Total Revenue'
    assert any(char.isdigit() for char in result[1])

def test_type_of_return():
    result = get_financials('MSFT', 'Total Revenue')
    assert isinstance(result, tuple)

def test_invalid_ticker():
    with pytest.raises(Exception):
        get_financials('INVALIDTICKER', 'Total Revenue')

def test_invalid_field():
    with pytest.raises(Exception):
        get_financials('MSFT', 'NotARealField')
