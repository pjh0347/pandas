# coding: utf-8

import pandas as pd
import numpy as np

df = pd.DataFrame([[1,1,1],[3,2,3],[3,2,4],[5,3,1],[1,np.nan,3],[1,np.nan,3],[1,10,10]], columns=['a','b','y'])

print "original"
print df

print "apply"
print df.groupby('a').apply(np.sum)

print "agg"
print df.groupby('a').agg(np.sum)

print "transform"
print df.groupby('a').transform(np.sum)

