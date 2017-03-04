# coding: utf-8

import pandas as pd

df = pd.DataFrame([[1,2],[3,4],[5,6]], columns=['a', 'b'])

print "original"
print df

print "drop (row)"
df = df.drop(1, axis=0)
print df

print "reindex"
print df.reset_index(drop=True)

