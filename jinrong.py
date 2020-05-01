import pandas as pd
CSV_FILE_PATH = './zhubiao.csv'
df1 = pd.read_csv(CSV_FILE_PATH,encoding='utf-8',)

CSV_FILE_PATH2 = './fuubiao.csv'
df2 = pd.read_csv(CSV_FILE_PATH,encoding='utf-8',)





print(df1,df2)
