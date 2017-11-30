# coding: utf-8

import pandas as pd

df1 = pd.DataFrame(range(1,6), index=pd.date_range('20170101', periods=5,), columns=['col'])
df2 = pd.DataFrame(range(12,17), index=pd.date_range('20170102', periods=5,), columns=['col'])

print "original : df1"
print df1

print "original : df2"
print df2

print "df1.combine_first(df2)  <--- df1 의 NaN 을 df2 로 채워넣기. (key 는 df1 & df2 합친 기준)"
print df1.combine_first(df2)

print "df1.update(df2)  <--- df1 을 df2(NaN 제외)로 채워 넣음. (inplace. key 는 df1 기준)"
df1.update(df2)
print df1

