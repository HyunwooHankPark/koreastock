import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 페이지 설정
st.set_page_config(page_title="한국 바이오 시총 Top10 기업 주가", layout="wide")
st.title("🧬 한국 바이오 시총 Top10 기업 최근 5년 주가 변동")

# 한국 바이오 시총 Top10 기업
bio_top10_tickers = {
    'Samsung Biologics': '207940.KS',
    'Celltrion': '068270.KS',
    'SK Bioscience': '302440.KS',
    'SK Biopharmaceuticals': '326030.KS',
    'Hanmi Pharmaceutical': '128940.KS',
    'Chong Kun Dang': '185750.KS',
    'Green Cross (GC)': '006280.KS',
    'Yuhan': '000100.KS',
    'Daewoong Pharmaceutical': '069620.KS',
    'LG Chem': '051910.KS'
}

# 기간 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=5*365)

# 데이터 다운로드 및 시각화
for name, ticker in bio_top10_tickers.items():
    try:
        df = yf.download(ticker, start=start_date, end=end_date)
        if df.empty:
            st.warning(f"{name} ({ticker}) 데이터가 없습니다.")
            continue

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name=name))
        fig.update_layout(title=f"{name} ({ticker}) 최근 5년 주가", xaxis_title="Date", yaxis_title="Close Price (KRW)")

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"{name} ({ticker}) 데이터 로딩 중 오류 발생: {e}")
