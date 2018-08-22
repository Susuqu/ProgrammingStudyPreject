# -*-coding:utf-8 -*-
from scipy import stats


def Chi2Contingency:



def Chi2Indep:




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