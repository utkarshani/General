import sys
#from StringIO import StringIO
import pandas as pd

df=pd.read_csv(r"KH032medication.csv")
#print(df.timestamp)

#df[df.timestamp]=pd.to_datetime(pd[df.timestamp], unit='ms').dt.tz_localize('UTC' ).dt.tz_convert('America/New_York')
#df[df.timestamp]=pd.DatetimeIndex(pd.to_datetime(pd[df.timestamp], unit='ms')).tz_localize('UTC' ).tz_convert('America/New_York')

df['datetime'] = pd.to_datetime(df["timestamp"], unit='ms')
#df['datetime']= pd.DatetimeIndex(df['timestamp']*10**9)
df.insert(6,'new',df.timestamp)
df.to_csv(r"KH032medication.csv")
print(df.timestamp)


#df.to_csv(r"KH032medication.csv")
