import random


import pandas as pd
CSV_FILE_PATH = './fubiao.csv'
df1 = pd.read_csv(CSV_FILE_PATH,encoding='utf-8',)



df1.replace("商务服务",int("5"),inplace = True)
print(df1)

#
# import uuid
# def getUUID():
#     return "".join(str(uuid.uuid1()).split("-")).upper()
# print(getUUID())




