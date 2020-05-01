import pandas as pd
import codecs
import sys
# import json
# reload(sys)
# sys.setdefaultencoding('utf-8')
# filename='sn-uid.xlsx'



# df1=pd.read_excel(filename,sheet_name='Sheet1')
# df2=pd.read_excel(filename,sheet_name='Sheet2')

# 获取指定字段
#print df1.columns
# df11 = df1.ix[:,['微信号/昵称','SN号','用户账号']]
# df11.columns = ['微信号/昵称','SN号','手机号']
# df22 = df2.ix[:,['用户id','手机号']]

# df3 = pd.merge(df11, df22, on='手机号', how='right').ix[:,['微信号/昵称','SN号','手机号','用户id']]
# values = df3.where(df3.notnull(), "").values

UID = {}
for item in values:
    UID[item[-1]] = [ str(i) for i in item[0:-1]]

with codecs.open("sn_uid.py", 'w', 'utf8') as wf:
     wf.write(json.dumps(UID, ensure_ascii=False))