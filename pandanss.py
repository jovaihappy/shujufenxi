import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import random

CSV_FILE_PATH = './fangyuan.csv'
df = pd.read_csv(CSV_FILE_PATH,encoding='utf-8',)

df['GOODS_ITEM_ID']=''
print(df)


# deposit_mode = [df["deposit_mode"].str.split("月租：")]
# print()


















# # df = df.iloc[:,3]  #获取列
#
# # li = [df["price"].str.split("付款方式：")]  切割方法
# li = [df["price"].str.split("付款方式：")]
#

