from pykrx import stock
import pandas as pd
from datetime import datetime, timedelta

# 조회 기간 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=5*365)

start = start_date.strftime('%Y%m%d')
end = end_date.strftime('%Y%m%d')

# 삼성바이오로직스 (207940)
df = stock.get_market_ohlcv_by_date(start, end, "207940")
print(df.head())
