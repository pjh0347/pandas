# coding: utf-8

import pandas as pd

df = pd.DataFrame([[1,2],[3,4],[5,6]], columns=['a', 'b'])

print "original"
print df

print "drop (col)"
print df.drop('a', axis=1)

print "drop (row)"
print df.drop(1, axis=0)

