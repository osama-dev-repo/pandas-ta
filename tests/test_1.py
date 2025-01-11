import pandas as pd
import pandas_ta as ta

df = pd.DataFrame() # Empty DataFrame

df = df.ta.ticker("aapl")

print(df.head())
