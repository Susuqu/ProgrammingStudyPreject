# -*-coding:utf-8 -*-

# @PROJECT  : ProgrammingStudyProject
# @Time     : 2018/08/22
# @Author   : Qu Susu
# @File     : def_description.py
# @Software : Pycharm

from scipy import stats
import numpy as np
from numpy import array,mean, median, ptp, var, std, cov, corrcoef
from scipy.stats import mode

def CheckDistribution(self):
    x_dis_pvalue = stats.anderson(self.x, dist='norm').critical_values.min()  # 对应统计显著性水平为15%
    y_dis_pvalue = stats.anderson(self.y, dist='norm').critical_values.min()
    '''
    AndersonResult(
    statistic=0.13676646631470035, 
    critical_values=array([0.507, 0.578, 0.693, 0.808, 0.961]), 
    significance_level=array([15. , 10. ,  5. ,  2.5,  1. ])
    )
    '''
    if (x_dis_pvalue or y_dis_pvalue) < 0.15:
        CheckOut = "Sorry. Your input x or y data doesn't conform to normal distribution, please check it first."
    else:
        CheckOut = "Congratulations. Your input x and y data both conform to normal distribution."

    self.CheckOut = CheckOut
    # print(self.CheckOut)
    return self


# 协方差cov和相关系数corrcoef
# data=table["adhdp"].dropna().sort_values().values #注意values后面没有括号
def descriptiveStat(data):
    # 中心位置（均值、中位数、众数）
    print(mean(data))
    print(median(data))
    print(mode(data))
    # 发散程度（方差、标准差、变异系数）
    print(var(data))
    print(std(data))
    cv=mean(data)/std(data)    #变异系数
    print(cv)
    # 偏差程度（Z-分数）
    Zscore=(data[0] - mean(data)) / std(data)
    print(Zscore)
