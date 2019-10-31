from alpha_vantage.timeseries import TimeSeries
from datetime import datetime

import os.path


def run():
    key = '1TKWNTNJE9BNAP7K'
    ts = TimeSeries(key)
    daily_peloton, daily_meta = ts.get_daily(symbol='PTON')
    monthly_peloton, monthly_meta = ts.get_monthly(symbol='PTON')

    create_file()

    today = datetime.today().strftime('%Y-%m-%d')
    daily_stock_data = daily_peloton.get(today)
    highest_price = 0
    for month in monthly_peloton:
        month_stock_data = monthly_peloton.get(month)
        high = month_stock_data.get('2. high')
        if highest_price < float(high):
            highest_price = float(high)
    if daily_stock_data:
        close = daily_stock_data.get('4. close')[:-2]
        high = daily_stock_data.get('2. high')[:-2]
        open_amt = daily_stock_data.get('1. open')[:-2]
        low = daily_stock_data.get('3. low')[:-2]
        content = "Peloton stock for %s:" % today + "\n"
        content += "\tOpened at: $" + open_amt + "\n"
        content += "\tClosed at: $" + close + "\n"
        content += "\tLow: $" + low + "\n"
        content += "\tHigh: $" + high + "\n"
        content += "Historical High: $" + str(highest_price) + "\n"

        content += "\n\n"
        if float(close) > 50.0:
            content += "SO RICH"
        else:
            content += "Not rich yet =("

        write_to_file(content)


def _get_name_of_file():
    save_path = '/Users/alson.lu/Desktop'

    name_of_file = "stock_prices"

    return os.path.join(save_path, name_of_file + ".txt")


def create_file():
    file1 = open(_get_name_of_file(), "w")

    file1.close()


def write_to_file(content):
    file1 = open(_get_name_of_file(), "w")

    file1.write(content)

    file1.close()


if __name__ == '__main__':
    run()
