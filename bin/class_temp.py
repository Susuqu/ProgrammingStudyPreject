# -*-coding:utf-8 -*-

# @PROJECT  : ProgrammingStudyProject
# @Time     : 2018/08/16
# @Author   : Qu Susu
# @File     : class_temp.py
# @Software : Pycharm

# ---------------------------All Packages-----------------------------
import argparse
import json
import numpy as np
import pandas as pd
from scipy import stats # Specific Packages
# ---------------------------Defining parameters----------------------
def get_args():
    '''
    命令行参数
    :return: args:
    '''
    parser=argparse.ArgumentParser(description='***Project 611 demo script: Basic Statistics Test Part***\n')
    parser.add_argument('--data', dest = 'Data', required = True, help = 'Your input data')
    parser.add_argument('--id', dest='Id', required=True, help = 'The job id.')
    parser.add_argument('--x', dest = 'X', required=True, help='Which column you want to test and use these column name as x input.')
    parser.add_argument('--y', dest='Y', required=True, help= 'Which column you want to test with x and use these column name as y input.')
    parser.add_argument('--method','-m', dest='Method_name',required=True, help = 'which Basic Statistic Test you want to use and input the corresponding method name, select the follow words as input: pears.')
    # # parser.add_argument('--use_default','-r', dest='Recommend_parameter', choices=['y', 'n'], help = 'Choose the default parameters or not!')

    args = parser.parse_args()
    return args
# ---------------------------Main program-----------------------------
class BasicStaTest:
    def __init__(self):
        # self.args=get_args()
        args = get_args()
        self.args=args.__dict__
        self.inputData = args.Data
        self.id = args.Id
        self.x = args.X
        self.y = args.Y
        self.method = args.Method_name
        # CheckOut is used to check if sample's distribution = norm
        self.CheckOut=''
        self.FinalResult={}
        # pass

    def data(self):
        self.inputData=pd.read_csv(self.inputData)
        return self

    def test(self):
        print('OK')
        return self

    def fillNA(self):
        fillNA_data = self.inputData.dropna().copy()
        fillNA_data['Gender'] = fillNA_data['Gender'].map({'Female': 1, 'Male': 0}).astype(int)
        # print(fillNA_data)
        self.inputData=fillNA_data
        return self

    def Choose_columns(self):
        x_columns_name_list = self.x.split(',')
        y_columns_name_list = self.y.split(',')
        x_Choose_data = np.array(self.inputData[x_columns_name_list]) #dataframe 转为array数据
        y_Choose_data = np.array(self.inputData[y_columns_name_list])
        self.x=x_Choose_data
        self.y=y_Choose_data
        return self

    def CheckDistribution(self):
        x_dis_pvalue=stats.anderson(self.x,dist='norm').critical_values.min()    #对应统计显著性水平为15%
        y_dis_pvalue=stats.anderson(self.y,dist='norm').critical_values.min()
        '''
        AndersonResult(
        statistic=0.13676646631470035, 
        critical_values=array([0.507, 0.578, 0.693, 0.808, 0.961]), 
        significance_level=array([15. , 10. ,  5. ,  2.5,  1. ])
        )
        '''
        if (x_dis_pvalue or y_dis_pvalue) < 0.15:
            CheckOut="Sorry. Your input x or y data doesn't conform to normal distribution, please check it first."
        else:
            CheckOut = "Congratulations. Your input x and y data both conform to normal distribution."

        self.CheckOut=CheckOut
        # print(self.CheckOut)
        return self

# -------------------------------calculate results------------------------------

    def Correlation(self):
        global result_dict
        global result
        if len(self.x)==len(self.y):
            if self.method=='pears':
                if 'Congratulations.'in self.CheckOut:
                    result = stats.pearsonr(self.x, self.y)
            elif self.method=='spearm':
                result = stats.spearmanr(self.x, self.y)

            result_dict={'Statistics':list(result[0]),'P-value':list(result[1])}
            # print(result_dict)
            self.FinalResult=result_dict
        else:
            print('Number of sample1 and sample2 should be equal.')
        return self
# -------------------generate 2 save json files: args & results------------------
    def SaveArgsJson(self):
        args_json = json.dumps(self.args)
        Saved_json_name = self.id + '_' + self.method + '_' + 'args.json'
        with open(Saved_json_name, 'w', encoding='utf-8') as json_file:
            json.dump(args_json, json_file, ensure_ascii=False)
        return self

    def SaveResultJson(self):
        result_dict_dump=json.dumps(self.FinalResult)
        Saved_json_name=self.id + '_' + self.method + '_' + 'results.json'
        with open(Saved_json_name, 'w', encoding='utf-8') as json_file:
            json.dump(result_dict_dump, json_file, ensure_ascii=False)
        return self

if __name__ == '__main__':
    obj=BasicStaTest()
    obj.data().fillNA().Choose_columns().CheckDistribution().Correlation().SaveArgsJson().SaveResultJson()  # Correlation(): test is OK