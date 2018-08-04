#!/usr/bin/env python3

#-------------------------------------------------------------------------
# Copyright (c) @pulkit.  
# Author: Pulkit Agrawal
# Date: 04 of Aug 2018
#--------------------------------------------------------------------------

import pandas as pd 
import numpy as np

df = pd.read_json('searches.json', lines=True)


df['design'] = np.where(df['uid'] %2==0, 'Old', 'New')

#print(df.loc[df.design == 'New', 'search_count'].sum())

#print(df.groupby(['design']).search_count.sum())

#print(df.groupby(['design']).login_count.sum())


df2 = df.groupby(['design']).agg({'search_count': 'sum', 'login_count': 'sum'})

print("\n",df2)
print("\n*******************Answer 1******************")
if df2['search_count']['Old'] > df2['search_count']['New']:
    print("More users uses search feature in old design(A).") 
else:
    print("More users uses search feature in new design(B).") 

print("\n***************Answer 2***************")
if df2['login_count']['Old'] > df2['login_count']['New']:
    print("User search more often in old design(A).") 
else:
    print("User search more often in New design(B).") 
    

