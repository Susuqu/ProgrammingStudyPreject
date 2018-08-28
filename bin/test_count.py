# -*-coding:utf-8 -*-

# @PROJECT  : ProgrammingStudyProject
# @Time     : 2018/08/28
# @Author   : Qu Susu
# @File     : test_count.py
# @Software : Pycharm

import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series


# list
a = [1, 2, 3, 1, 1, 2]
b=['china','china','test','love','peace','love','test']
mylist=set(b)
for item in mylist:
    print(item+'\t'+str(b.count(item)))

# dict


# dataframe or series, pandas下的value_counts()不仅可以统计list中各个元素的个数，还可以对矩阵元素进行统计
series_b=Series(b)
print(series_b.value_counts())

c = pd.DataFrame([[1,2,3],
                  [3,1,3],
                  [1,2,1]])
c_count=c.apply(pd.value_counts)
print(c_count)