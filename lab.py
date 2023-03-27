import pandas as pd
import numpy as np
exam_data={'name':['Anastasia','dima','katherine','james','emily','micheal','matthew','laura','kevin','jones'],
           'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
           'attempts':[1,3,2,3,2,3,1,1,2,1],
           'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']}
labels=['a','b','c','d','e','f','g','h','i','j']


df = pd.DataFrame(exam_data, index=labels)
x=pd.DataFrame(exam_data)
print(x)
tot_rows=len(df.axes[0])
tot_cols=len(df.axes[1])
print("\n")
print("number of Rows:",str(tot_rows))
print("number of columns:",str(tot_cols))
