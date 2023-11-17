import ccxt
import pprint
import pandas as pd
import winsound
import time ## for sleep // time_now
import os ## for os.chdir

dir = 'C:/Users/user/Desktop/binance_bebe'
os.chdir(dir)

with open("binance_api_secret.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret_key = lines[1].strip()

binance = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret_key,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})


# 알림음 재생
def beepup():
    winsound.Beep(
        frequency=2000,  # Hz
        duration=500  # milliseconds
        )

def beepdn():
    winsound.Beep(
        frequency=400,  # Hz
        duration=500  # milliseconds
        )

def beep():
    winsound.Beep(
        frequency=400,  # Hz
        duration=500  # milliseconds
        )

def add_log(content):
    f=open("log.txt","a+")
    f.write(content)
    f.close()




# for i in range(1,11):
while True:
    # previous data
    btc = binance.fetch_ohlcv(
        symbol="BTC/USDT", 
        timeframe='4h', 
        since=None, 
        limit=1)
    ##
    df = pd.DataFrame(btc, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df.set_index('datetime', inplace=True)
    print(df)
    ##
    open_pr = df['open'][0]
    close_pr = df['close'][0]
    print('now_price: ',close_pr)
    ##
    time_now = time.strftime('%Y.%m.%d - %H:%M:%S')
    ##
    delta_pro = (close_pr - open_pr) / open_pr * 100
    print('delta_%: ',delta_pro)
    wlog = str(time_now) + ' || now_price: ' + str(close_pr) + ' || delta_%: ' + str(delta_pro) + '\n'
    if delta_pro >= 4:
        add_log(wlog)
        beepup();beepup()
    elif delta_pro >= 2:
        add_log(wlog)
        beepup()
    elif delta_pro <= -4:
        add_log(wlog)
        beepdn();beepdn()
    elif delta_pro <= -2:
        add_log(wlog)
        beepdn()
    else:
        print('======== No Event ( 지켜보고있다 ) ========')
        # beep()
    ##
    ##
    ##
    time.sleep(15)




'''
git init
git add .
git status
git commit -m "binance_monitor_v1"
git remote add origin git@github.com:jwyunmd/binance_monitor_first.git
(if error)$git remote remove origin
git remote -v
git push
'''





