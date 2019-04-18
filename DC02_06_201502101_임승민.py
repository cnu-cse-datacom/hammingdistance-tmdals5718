import random
import numpy as np
import pandas as pd
from hamming_parctice import hamming

df = pd.read_csv('sample.csv',names=['word','bin'])

m_d = hamming(df.iloc[0,1],df.iloc[1,1]);


count = 1
for i in range(0,len(df)):
    for j in range(0,len(df)):
        if i < j:
            dist = hamming(df.iloc[i,1], df.iloc[j,1])
            print(count,"(",df.iloc[i,0],df.iloc[j,0],") hamming_distance :" ,dist )
            if m_d > dist:
                m_d = dist
            count = count +1
print("min hamming distance",m_d)
