# -*-coding:utf-8 -*-
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from scipy import stats

def ExampleData(dataNum):
    '''
    :param dataNum: 1/2/other number
    :return: df (example data frame for calculating correlation and corr plot)
    '''
    if dataNum==1:
        df=pd.DataFrame({'A':np.random.randint(1,100,10),
                         'B':np.random.randint(1,100,10),
                         'C': np.random.randint(1, 100, 10)})
        print(df)
    elif dataNum==2:
        np.random.seed(0)
        df=np.random.rand(10, 12)
        print(df)
    else:
        df_long=sns.load_dataset("flights")
        df=df_long.pivot("month", "year", "passengers") #透视表功能，说白了就是像excle的计数
        # df_long.head()
        # df.head()

def StudentTtest(x,y):
    result=stats.mstats.ttest_ind(x,y)
    # result_dict = {'Statistics': list(result[0]), 'P-value': list(result[1])}
    return result

if __name__=='__main__':
    # x=[1,12,30,50,70]
    # y=[10,25,25,62,62,98,100,45]
    # print(StudentTtest(x,y))
    # x_array=np.array(x)
    # print(x_array.var())
    # y_array=np.array(y)
    # print(y_array.var())
    x=np.array([[16, 18, 16, 14, 12, 12], [32, 24, 16, 28, 20, 24], [32, 24, 16, 25, 20, 24]]).T
    print(x.shape)
    print(stats.mstats.chisquare(x))