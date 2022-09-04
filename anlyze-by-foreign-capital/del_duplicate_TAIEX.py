import pandas as pd

df_new = []
with open('./data/TAIEX.csv', 'r') as f:
    df = pd.read_csv(f)
    for i in range(0, df.shape[0]):
        if df.iloc[i]['Date'] == df.iloc[i-1]['Date']:
            df_new.append(df.iloc[i])

df_new = pd.DataFrame(df_new)

with open('data/TAIEX-wo-duplicate.csv', 'w', newline="") as f:
    df_new.to_csv(f, index=False)
