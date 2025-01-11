import pandas as pd
import pandas_ta_remake as ta

df = pd.DataFrame() # Empty DataFrame

df = df.ta.ticker("aapl")

df.ta.ema(leangh=14, append=True)
print(df.dropna().head())
