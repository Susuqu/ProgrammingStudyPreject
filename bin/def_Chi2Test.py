# -*-coding:utf-8 -*-
import numpy as np
from scipy import stats
import sys

# ----------------------------------------------------------------------------
# 拟合优度检验是用于分析实际次数与理论次数是否相同，适用于单个因素分类的计数数据。卡方拟合度检验用于判断不同类型结果的比例分布相对于一个期望分布的拟合程度。
# 例如：随机抽取60名高一学生，问他们文理要不要分科，回答赞成的39人，反对的21人，问对分科的意见是否有显著的差异。

# When f_obs is 2-D, by default the test is applied to each column (this is different from the stats.chi2_contingency).
    # obs = np.array([[16, 18, 16, 14, 12, 12], [32, 24, 16, 28, 20, 24]]).T
    # obs.shape #(6, 2)
    # stats.chisquare(obs) # (array([ 2. ,  6.66666667]), array([ 0.84914504,  0.24663415]))

def Chi2Fitting(data,alpha,sp):
    chis,p_value=stats.chisquare(data,axis=sp)
    # out: (2.0, 0.84914503608460956)
    i,j=data.shape  #j为自由度
    # print(data.shape)
    # print(chis)

    if j==0:
        print('自由度应该大于等于1')
    elif j==1:
        cv=stats.chi2.isf(alpha*0.5,j) 
    else:
        cv = stats.chi2.isf(alpha * 0.5, j-1)

    if chis>cv:
        re=1 # 拒绝原假设，即类别A与B的比例有显著差异
    else:
        re=0 # 表示接受原假设

    return chis,p_value,cv,j-1,re

# test
data4=np.array([[39,21,11,34]])
# print(Chi2Fitting(data4,alpha=0.05,sp=0))
print(Chi2Fitting(data4,alpha=0.05,sp=None))
#By setting axis=None, the test is applied to all data in the array(are treated as a single data set), which is equivalent to applying the test to the flattened array.

# sys.exit()
# ----------------------------------------------------------------------------
# 独立性检验用于分析各有多项分类的两个或两个以上的因素之间是否有关联或是否独立的问题。
def Chi2Indep(data,alpha):
    chis,p_value,j,expect=stats.chi2_contingency(data)

    if j==0:
        print('自由度应该大于等于1')
    elif j == 1:
        cv = stats.chi2.isf(alpha * 0.5, j)
    else:
        cv= stats.chi.isf(alpha * 0.5, j-1)

    if chis>cv:
        re=1 # 拒绝原假设，即类别A与B的比例有显著差异
    else:
        re=0 # 表示接受原假设

    return chis,p_value,j,expect,re

# test a two-way example:
# 3x3，两个类别，每个类别有3个水平，具体数字表示的是频数
data2=np.array([[10, 10, 20], [20, 20, 20], [30, 15, 20]])
print(data2.shape)
chis2,p_value2,j2,expect2,re2=Chi2Indep(data2,alpha=0.05)
print(chis2,p_value2,j2,expect2,re2,end='\n')

# test a four-way example (2x2x2x2)
data3=np.array(
                [[[[12, 17],
                [11, 16]],
                [[11, 12],
                [15, 16]]],
                [[[23, 15],
                [30, 22]],
                [[14, 17],
                [15, 16]]]])
chis3,p_value3,j3,expect3,re3=Chi2Indep(data3,alpha=0.05)
print(chis3,p_value3,j3,expect3,re3,end='\n')
