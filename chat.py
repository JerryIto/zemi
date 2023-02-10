from numpy import reciprocal
import requests
import json
import datetime
import streamlit as st

st.title('為替表示:一週間平均')

# Open Exchange RatesのAPIキーを設定
app_id = 'f982ac5b81d74f84952cb0e46639a459'

# 10日間の為替レートを取得
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=10)

url = f'https://openexchangerates.org/api/historical/{start_date.strftime("%Y-%m-%d")}.json?app_id={app_id}'

response = requests.get(url)
data = json.loads(response.text)

# 円とドルの為替レートを取得
jpy_rate = data['rates']['JPY']
usd_rate = data['rates']['USD']

# 平均為替レートを計算
average_rate = usd_rate / jpy_rate
average_rate = reciprocal(average_rate)
# 結果を出力
print(f'1ドルに対する円の10日間の平均為替レート: {average_rate}')

st.write(average_rate)

