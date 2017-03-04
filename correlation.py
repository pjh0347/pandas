# coding: utf-8

import pandas as pd

df1 = pd.DataFrame([[1,2],[2,3],[9,4]], columns=['a','b'])
df2 = pd.DataFrame([[9,2],[2,3],[1,4]], columns=['a','b'])

print "original : df1"
print df1
print "original : df2"
print df2

print "corr ( col <-> col )"
print df1['a'].corr(df2['b'])

print "corrwith ( df <-> df )"
print df1.corrwith(df2)

