# coding: utf-8

import pandas as pd

df = pd.DataFrame(range(5), index=pd.date_range('20170101', periods=5,), columns=['col'])

print "original : df"
print df

print "slice : df[:2]"
print df[:2]

print "slice : df[:'20170103']"
print df[:'20170103']

print "iloc : df.iloc[:2]"
print df.iloc[:2]

print "loc : df.loc[:'20170103']"
print df.loc[:'20170103']

print "ix : df.ix[:2]"
print df.ix[:2]

print "ix : df.ix[:'20170103']"
print df.ix[:'20170103']
