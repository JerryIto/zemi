from numpy import reciprocal
import requests
import json
import datetime
import pandas as pd
import streamlit as st

st.title('一週間平均（一万円換算）')

# Open Exchange RatesのAPIキーを設定
app_id = 'f982ac5b81d74f84952cb0e46639a459'

# 10日間の為替レートを取得
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=7)
#１ヶ月の為替レートを取得
end_date1 = datetime.datetime.now()
start_date1 = end_date - datetime.timedelta(days=30)

url = f'https://openexchangerates.org/api/historical/{start_date.strftime("%Y-%m-%d")}.json?app_id={app_id}'
url1 = f'https://openexchangerates.org/api/historical/{start_date1.strftime("%Y-%m-%d")}.json?app_id={app_id}'

response = requests.get(url)
data = json.loads(response.text)

response1 = requests.get(url1)
data1 = json.loads(response1.text)

# 円とドルの為替レートを取得
jpy_rate = data['rates']['JPY']
usd_rate = data['rates']['USD']#ドル
uae_rate = data['rates']['AED']#ディルハム
#afn_rate = data['rates']['AFN']#アフガニ
#all_rate = data['rates']['ALL']#レク
#amd_rate = data['rates']['AMD']#ドラム
#ang_rate = data['rates']['ANG']#ギルター
aoa_rate = data['rates']['AOA']#クワンザ
ars_rate = data['rates']['ARS']#ペソ
aud_rate = data['rates']['AUD']#オーストラリアドル
#awg_rate = data['rates']['AWG']#フロリン
azn_rate = data['rates']['ARS']#アゼルバイジャン・マナト

bam_rate = data['rates']['BAM']#マルク
#bbd_rate = data['rates']['BBD']#バルバトス・ドル
bdt_rate = data['rates']['BDT']#タカ
bgn_rate = data['rates']['BGN']#レフ
bhd_rate = data['rates']['BHD']#バーレーン・ディナール
#bif_rate = data['rates']['BIF']#ブルンジ・フラン
#bmd_rate = data['rates']['BMD']#バミューダ・ドル
#bob_rate = data['rates']['BOB']#ボリビアーノ
brl_rate = data['rates']['BRL']#レアル
#bsd_rate = data['rates']['BD']#バハマ・ドル
btn_rate = data['rates']['BTN']#ニュルタム
#bwp_rate = data['rates']['BWP']#プラ
#bzd_rate = data['rates']['BZD']#ベリーズ・ドル

cad_rate = data['rates']['CAD']#カナダ・ドル
chf_rate = data['rates']['CHF']#スイス・フラン
clf_rate = data['rates']['CLF']#チリ・ペソ
cny_rate = data['rates']['CNY']#元
cop_rate = data['rates']['COP']#コロンビア・ペソ
cup_rate = data['rates']['CUP']#キューバ・ペソ
czk_rate = data['rates']['CZK']#コルナ

dkk_rate = data['rates']['DKK']#クローネ
dop_rate = data['rates']['DOP']#ドミニカ・ペソ

egp_rate = data['rates']['EGP']#エジプト・ポンド
eur_rate = data['rates']['EUR']#ユーロ

gbp_rate = data['rates']['GBP']#ポンド
ghs_rate = data['rates']['GHS']#セディ

hkd_rate = data['rates']['HKD']#香港・ドル
hrk_rate = data['rates']['HRK']#クーナ
huf_rate = data['rates']['HUF']#フォリント

idr_rate = data['rates']['IDR']#ルピア
inr_rate = data['rates']['INR']#ルピー
isk_rate = data['rates']['ISK']#アイスランド

jmd_rate = data['rates']['JMD']#ジャマイカ・ドル

khr_rate = data['rates']['KHR']#カンボジア
krw_rate = data['rates']['KRW']#韓国

lkr_rate = data['rates']['LKR']#スリランカ

mad_rate = data['rates']['MAD']#モロッコ
mga_rate = data['rates']['MGA']#マダガスカル
mnt_rate = data['rates']['MNT']#モンゴル
mop_rate = data['rates']['MOP']#マカオ
mvr_rate = data['rates']['MVR']#モルディブ
mxn_rate = data['rates']['MXN']#メキシコ
mzn_rate = data['rates']['MZN']#モザンピーク

nok_rate = data['rates']['NOK']#ノルウェー

sek_rate = data['rates']['SEK']#スウェーデン
sgd_rate = data['rates']['SGD']#シンガポール

thb_rate = data['rates']['THB']#タイ
try_rate = data['rates']['TRY']#トルコ
twd_rate = data['rates']['TWD']#スイス・フラン

vnd_rate = data['rates']['VND']#ベトナム

# 円とドルの為替レートを取得（１ヶ月）
jpy_rate1 = data1['rates']['JPY']
usd_rate1 = data1['rates']['USD']#ドル
uae_rate1 = data1['rates']['AED']#ディルハム
#afn_rate1 = data1['rates']['AFN']#アフガニ
#all_rate1 = data1['rates']['ALL']#レク
#amd_rate1 = data1['rates']['AMD']#ドラム
#ang_rate1 = data1['rates']['ANG']#ギルター
aoa_rate1 = data1['rates']['AOA']#クワンザ
ars_rate1 = data1['rates']['ARS']#ペソ
aud_rate1 = data1['rates']['AUD']#オーストラリアドル
#awg_rate1 = data1['rates']['AWG']#フロリン
azn_rate1 = data1['rates']['ARS']#アゼルバイジャン・マナト

bam_rate1 = data1['rates']['BAM']#マルク
#bbd_rate1 = data1['rates']['BBD']#バルバトス・ドル
bdt_rate1 = data1['rates']['BDT']#タカ
bgn_rate1 = data1['rates']['BGN']#レフ
bhd_rate1 = data1['rates']['BHD']#バーレーン・ディナール
#bif_rate1 = data1['rates']['BIF']#ブルンジ・フラン
#bmd_rate1 = data1['rates']['BMD']#バミューダ・ドル
#bob_rate1 = data1['rates']['BOB']#ボリビアーノ
brl_rate1 = data1['rates']['BRL']#レアル
#bsd_rate1 = data1['rates']['BD']#バハマ・ドル
btn_rate1 = data1['rates']['BTN']#ニュルタム
#bwp_rate1 = data1['rates']['BWP']#プラ
#bzd_rate1 = data1['rates']['BZD']#ベリーズ・ドル

cad_rate1 = data1['rates']['CAD']#カナダ・ドル
chf_rate1 = data1['rates']['CHF']#スイス・フラン
clf_rate1 = data1['rates']['CLF']#チリ・ペソ
cny_rate1 = data1['rates']['CNY']#元
cop_rate1 = data1['rates']['COP']#コロンビア・ペソ
cup_rate1 = data1['rates']['CUP']#キューバ・ペソ
czk_rate1 = data1['rates']['CZK']#コルナ

dkk_rate1 = data1['rates']['DKK']#クローネ
dop_rate1 = data1['rates']['DOP']#ドミニカ・ペソ

egp_rate1 = data1['rates']['EGP']#エジプト・ポンド
eur_rate1 = data1['rates']['EUR']#ユーロ

gbp_rate1 = data1['rates']['GBP']#ポンド
ghs_rate1 = data1['rates']['GHS']#セディ

hkd_rate1 = data1['rates']['HKD']#香港・ドル
hrk_rate1 = data1['rates']['HRK']#クーナ
huf_rate1 = data1['rates']['HUF']#フォリント

idr_rate1 = data1['rates']['IDR']#ルピア
inr_rate1 = data1['rates']['INR']#ルピー
isk_rate1= data1['rates']['ISK']#アイスランド

jmd_rate1 = data1['rates']['JMD']#ジャマイカ・ドル

khr_rate1 = data1['rates']['KHR']#カンボジア
krw_rate1 = data1['rates']['KRW']#韓国

lkr_rate1 = data1['rates']['LKR']#スリランカ

mad_rate1 = data1['rates']['MAD']#モロッコ
mga_rate1 = data1['rates']['MGA']#マダガスカル
mnt_rate1 = data1['rates']['MNT']#モンゴル
mop_rate1 = data1['rates']['MOP']#マカオ
mvr_rate1 = data1['rates']['MVR']#モルディブ
mxn_rate1 = data1['rates']['MXN']#メキシコ
mzn_rate1 = data1['rates']['MZN']#モザンピーク

nok_rate1 = data1['rates']['NOK']#ノルウェー

sek_rate1 = data1['rates']['SEK']#スウェーデン
sgd_rate1 = data1['rates']['SGD']#シンガポール

thb_rate1 = data1['rates']['THB']#タイ
try_rate1 = data1['rates']['TRY']#トルコ
twd_rate1 = data1['rates']['TWD']#スイス・フラン

vnd_rate1 = data1['rates']['VND']#ベトナム


# 平均為替レートを計算(一週間)
average_rate = (jpy_rate / usd_rate)*0.0001
average_rate = reciprocal(average_rate)

average_rate1 = (jpy_rate/uae_rate )*0.0001
average_rate1 = reciprocal(average_rate1)

average_rate2 = (jpy_rate/aud_rate )*0.0001
average_rate2 = reciprocal(average_rate2)

average_rate3 = (jpy_rate/bam_rate )*0.0001
average_rate3 = reciprocal(average_rate3)

average_rate4 = (jpy_rate/bdt_rate )*0.0001
average_rate4 = reciprocal(average_rate4)

average_rate5 = (jpy_rate/bgn_rate )*0.0001
average_rate5 = reciprocal(average_rate5)

average_rate6 = (jpy_rate/brl_rate )*0.0001
average_rate6 = reciprocal(average_rate6)

average_rate7 = (jpy_rate/btn_rate )*0.0001
average_rate7 = reciprocal(average_rate7)

#average_rate8 = byr_rate / jpy_rate
#average_rate8 = reciprocal(average_rate8)

#average_rate9 = bzd_rate / jpy_rate
#average_rate9 = reciprocal(average_rate9)

average_rate10 = (jpy_rate/cad_rate )*0.0001
average_rate10 = reciprocal(average_rate10)

average_rate11 = (jpy_rate/chf_rate )*0.0001
average_rate11 = reciprocal(average_rate11)

average_rate12 = (jpy_rate/cny_rate )*0.0001
average_rate12 = reciprocal(average_rate12)

average_rate13 = (jpy_rate/cop_rate )*0.0001
average_rate13 = reciprocal(average_rate13)

average_rate14 = (jpy_rate/cup_rate )*0.0001
average_rate14 = reciprocal(average_rate14)

average_rate15 = (jpy_rate/cup_rate )*0.0001
average_rate15 = reciprocal(average_rate15)

average_rate16 = (jpy_rate/czk_rate )*0.0001
average_rate16 = reciprocal(average_rate16)

average_rate17 = (jpy_rate/dkk_rate )*0.0001
average_rate17 = reciprocal(average_rate17)

average_rate18 = (jpy_rate/dop_rate )*0.0001
average_rate18 = reciprocal(average_rate18)

average_rate19 = (jpy_rate/egp_rate )*0.0001
average_rate19 = reciprocal(average_rate19)

average_rate20 = (jpy_rate/eur_rate )*0.0001
average_rate20 = reciprocal(average_rate20)

average_rate21 = (jpy_rate/gbp_rate )*0.0001
average_rate21 = reciprocal(average_rate21)

average_rate22 = (jpy_rate/ghs_rate )*0.0001
average_rate22 = reciprocal(average_rate22)

average_rate23 = (jpy_rate/hkd_rate )*0.0001
average_rate23 = reciprocal(average_rate23)

average_rate24 = (jpy_rate/hrk_rate )*0.0001
average_rate24 = reciprocal(average_rate24)

average_rate25 = (jpy_rate/huf_rate )*0.0001
average_rate25 = reciprocal(average_rate25)

average_rate26 = (jpy_rate/idr_rate )*0.0001
average_rate26 = reciprocal(average_rate26)

average_rate27 = (jpy_rate/inr_rate )*0.0001
average_rate27 = reciprocal(average_rate27)

average_rate28 = (jpy_rate/isk_rate )*0.0001
average_rate28 = reciprocal(average_rate28)

average_rate29 = (jpy_rate/isk_rate )*0.0001
average_rate29 = reciprocal(average_rate29)

average_rate30 = (jpy_rate/jmd_rate )*0.0001
average_rate30 = reciprocal(average_rate30)

average_rate31 = (jpy_rate/krw_rate )*0.0001
average_rate31 = reciprocal(average_rate31)

average_rate32 = (jpy_rate/lkr_rate )*0.0001
average_rate32 = reciprocal(average_rate32)

average_rate33 = (jpy_rate/mvr_rate )*0.0001
average_rate33 = reciprocal(average_rate33)

average_rate34 = (jpy_rate/mxn_rate )*0.0001
average_rate34 = reciprocal(average_rate34)

# 平均為替レートを計算(１ヶ月)
average_rate0 = (jpy_rate1 / usd_rate1)*0.0001
average_rate0 = reciprocal(average_rate0)

average_rate01 = (jpy_rate1/uae_rate1 )*0.0001
average_rate01 = reciprocal(average_rate01)

average_rate02 = (jpy_rate1/aud_rate1 )*0.0001
average_rate02 = reciprocal(average_rate02)

average_rate03 = (jpy_rate1/bam_rate1 )*0.0001
average_rate03 = reciprocal(average_rate03)

average_rate04 = (jpy_rate1/bdt_rate1)*0.0001
average_rate04 = reciprocal(average_rate04)

average_rate05 = (jpy_rate1/bgn_rate1 )*0.0001
average_rate05 = reciprocal(average_rate05)

average_rate06 = (jpy_rate1/brl_rate1 )*0.0001
average_rate06 = reciprocal(average_rate06)

average_rate07 = (jpy_rate1/btn_rate1 )*0.0001
average_rate07 = reciprocal(average_rate07)

#average_rate08 = byr_rate / jpy_rate
#average_rate08 = reciprocal(average_rate8)

#average_rate09 = bzd_rate / jpy_rate
#average_rate09 = reciprocal(average_rate9)

average_rate010 = (jpy_rate1/cad_rate1 )*0.0001
average_rate010 = reciprocal(average_rate010)

average_rate011 = (jpy_rate1/chf_rate1 )*0.0001
average_rate011 = reciprocal(average_rate011)

average_rate012 = (jpy_rate1/cny_rate1 )*0.0001
average_rate012 = reciprocal(average_rate012)

average_rate013 = (jpy_rate1/cop_rate1 )*0.0001
average_rate013 = reciprocal(average_rate013)

average_rate014 = (jpy_rate1/cup_rate1)*0.0001
average_rate014 = reciprocal(average_rate014)

average_rate015 = (jpy_rate1/cup_rate1 )*0.0001
average_rate015 = reciprocal(average_rate015)

average_rate016 = (jpy_rate1/czk_rate1 )*0.0001
average_rate016 = reciprocal(average_rate016)

average_rate017 = (jpy_rate1/dkk_rate1 )*0.0001
average_rate017 = reciprocal(average_rate017)

average_rate018 = (jpy_rate1/dop_rate1 )*0.0001
average_rate018 = reciprocal(average_rate018)

average_rate019 = (jpy_rate1/egp_rate1 )*0.0001
average_rate019 = reciprocal(average_rate019)

average_rate020 = (jpy_rate1/eur_rate1 )*0.0001
average_rate020 = reciprocal(average_rate020)

average_rate021 = (jpy_rate1/gbp_rate1 )*0.0001
average_rate021 = reciprocal(average_rate021)

average_rate022 = (jpy_rate1/ghs_rate1 )*0.0001
average_rate022 = reciprocal(average_rate022)

average_rate023 = (jpy_rate1/hkd_rate1 )*0.0001
average_rate023 = reciprocal(average_rate023)

average_rate024 = (jpy_rate1/hrk_rate1 )*0.0001
average_rate024 = reciprocal(average_rate024)

average_rate025 = (jpy_rate1/huf_rate1 )*0.0001
average_rate25 = reciprocal(average_rate025)

average_rate026 = (jpy_rate1/idr_rate1 )*0.0001
average_rate026 = reciprocal(average_rate026)

average_rate027 = (jpy_rate1/inr_rate1 )*0.0001
average_rate027 = reciprocal(average_rate027)

average_rate028 = (jpy_rate1/isk_rate1 )*0.0001
average_rate028 = reciprocal(average_rate028)

average_rate029 = (jpy_rate1/isk_rate1 )*0.0001
average_rate029 = reciprocal(average_rate029)

average_rate030 = (jpy_rate1/jmd_rate1 )*0.0001
average_rate030 = reciprocal(average_rate030)

average_rate031 = (jpy_rate1/krw_rate1 )*0.0001
average_rate031 = reciprocal(average_rate031)

average_rate032 = (jpy_rate1/lkr_rate1 )*0.0001
average_rate032 = reciprocal(average_rate032)

average_rate033 = (jpy_rate1/mvr_rate1 )*0.0001
average_rate033 = reciprocal(average_rate033)

average_rate034 = (jpy_rate1/mxn_rate1 )*0.0001
average_rate034 = reciprocal(average_rate034)


# 結果を出力

#データフレーム作成
data={'アメリカ':[average_rate],'UAE':[average_rate1],'オーストラリア':[average_rate2],
       'ボスニア・ヘルツェゴビナ':[average_rate3],'バングラデシュ':[average_rate4],'ブルガリア':[average_rate5],
       'ブラジル':[average_rate6],'ブータン':[average_rate7],'カナダ':[average_rate10],
       'スイス':[average_rate11],'中国':[average_rate12],'コロンビア':[average_rate14],
       'キューバ':[average_rate15],'チェコ':[average_rate16],'デンマーク':[average_rate17],}
df = pd.DataFrame.from_dict(data)

data1={'アメリカ':[average_rate0],'UAE':[average_rate01],'オーストラリア':[average_rate02],
       'ボスニア・ヘルツェゴビナ':[average_rate03],'バングラデシュ':[average_rate04],'ブルガリア':[average_rate05],
       'ブラジル':[average_rate06],'ブータン':[average_rate07],'カナダ':[average_rate010],
       'スイス':[average_rate011],'中国':[average_rate012],'コロンビア':[average_rate014],
       'キューバ':[average_rate015],'チェコ':[average_rate016],'デンマーク':[average_rate017],}
df1 = pd.DataFrame.from_dict(data1)

st.write(df)

st.title('一ヶ月平均（一万円換算）')
st.write(df1)


