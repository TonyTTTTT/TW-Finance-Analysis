import pandas as pd

with open('./data/TAIEX.csv', 'r+') as f:
    df = pd.read_csv(f)
    diffs = [0]
    for i in range(1, df.shape[0]):
        diff = round(df.iloc[i]['Open'] - df.iloc[i-1]['Open'], 2)
        diffs.append(diff)
    df_new = df.copy()

df_new['Diff'] = diffs

with open('./data/TAIEX-diff.csv', 'w', newline="") as f:
    df_new.to_csv(f, index=False)