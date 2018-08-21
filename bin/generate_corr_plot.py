# -*-coding:utf-8 -*-

# @PROJECT  : plot test
# @Time     : 2018/08/21 update
# @Author   : Qu Susu
# @File     : generate_corr_plot.py
# @Software : Pycharm

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def ExampleData(dataNum):
    '''
    :param dataNum: 1/2/other number
    :return: df (example data frame for calculating correlation and corr plot)
    '''
    if dataNum==1:
        df=pd.DataFrame({'A':np.random.randint(1,100,10),
                         'B':np.random.randint(1,100,10),
                         'C':np.random.randint(1,100,10)})
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
    '''
    df_long:
         year      month  passengers
        0    1949    January         112
        1    1949   February         118
        2    1949      March         132
        3    1949      April         129
    '''
    '''
    df:
        year      1949  1950  1951  1952  1953  ...   1956  1957  1958  1959  1960
        month                                   ...                               
        January    112   115   145   171   196  ...    284   315   340   360   417
        February   118   126   150   180   196  ...    277   301   318   342   391
        March      132   141   178   193   236  ...    317   356   362   406   419
    '''
    return df

# ------------------------------------------------------------------------
def PlotCorr(df,method):
    '''
    :param df: data frame
    :param method: pearson/spearman/kendall
    :return:
    '''
    dfResult=df.corr(method=method)
    f,ax=plt.subplots(figsize=(4,4))
    sns.set()  # 调用sns中的函数
    sns.heatmap(dfResult,ax=ax,annot=True,vmin=0,vmax=1,square=True,center=0.5,cmap='rainbow')
    label_y = ax.get_yticklabels()
    plt.setp(label_y, rotation=360, horizontalalignment='right')
    label_x = ax.get_xticklabels()
    plt.setp(label_x, rotation=45, horizontalalignment='right')
    plt.savefig('../pic' + os.sep + '{}_{}'.format(method, 'corr.png'))
    plt.show()

if __name__=='__main__':
    df=ExampleData(dataNum=1)
    PlotCorr(df,method='pearson')
    PlotCorr(df, method='spearman')
    PlotCorr(df, method='kendall')