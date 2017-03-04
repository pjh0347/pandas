# coding: utf-8

import pandas as pd

df = pd.DataFrame([1,2,3,4,5], columns=['col'])

print "original : df"
print df

print "slice : df[:2]"
print df[:2]

print "iloc : df.iloc[:2]"
print df.iloc[:2]

print "loc : df.loc[:2]"
print df.loc[:2]

print "ix : df.ix[:2]"
print df.ix[:2]

