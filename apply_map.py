# coding: utf-8

import pandas as pd
import numpy as np

df = pd.DataFrame([[1,1,1],[3,2,3],[3,2,4],[5,3,1],[1,np.nan,3],[1,np.nan,3],[1,10,10]], columns=['a','b','y'])

print "original"
print df

print "df.apply(np.sum) : apply function to each column"
print df.apply(np.sum)

print "df.apply(np.sum, axis=1) : apply function to each crow"
print df.apply(np.sum, axis=1)

print "df['a'].map(lambda x: x == 1) : element-wise on a Series."
print df['a'].map(lambda x: x == 1)

print "df['a'].apply(lambda x: x == 1) : For applying more complex functions(NumPy/Python) on a Series"
print df['a'].apply(lambda x: x == 1)

print "df.applymap(lambda x: pd.isnull(x)) : Apply a function elementwise on a whole DataFrame"
print df.applymap(lambda x: pd.isnull(x))

