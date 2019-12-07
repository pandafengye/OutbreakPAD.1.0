from .Detection import Detection
from .Prediction import outbreak_prediction
#from .pad import pad
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
def PredictionDetection(data,n,p,d,q,std=0.02,a=["ARIMA-GRNN","ARIMA"]):
 #   Detection={};recent_data={}
##    global data_pre_all#定义全局变量
#    std 是GRNN的最佳平滑因子参数
   #####################################################    预测    ####################################################
    """数据在第n天暴发，所以将n-4前的数据预测第n天的数据以及检测其暴发"""
    if a=="ARIMA-GRNN":
        Prediction_data,outbreak_before,outbreak_after=outbreak_prediction(outbreak_index=n,data=data,p=p,d=d,q=q,std=std,a="ARIMA-GRNN")
        #data_pre_all=[]
        #for i,j in zip(range(len(range(outbreak_before,outbreak_after-3))),range(outbreak_before,outbreak_after-3)):
 #           print("检测从第"+str(j)+"数据开始预测的数据")
        #    data_pre=np.append(data[:j],ARIMA_GRNN_data[i])
        #    data_pre_all.append(data_pre)
    if a=="ARIMA":
        #print("ARIMA MODEL")
        Prediction_data,outbreak_before,outbreak_after=outbreak_prediction(outbreak_index=n,data=data,p=p,d=d,q=q,a="ARIMA")
    data_pre_all=[];df=pd.DataFrame()
    for i,j in zip(range(len(range(outbreak_before,outbreak_after-3))),range(outbreak_before,outbreak_after-3)):
 #           print("检测从第"+str(j)+"数据开始预测的数据")
        data_pre=np.append(data[:j],Prediction_data[i])
        data_pre_all.append(data_pre)
        df[str(j)]=data_pre
    df.index=data.index[:len(df)]
    df.to_csv("./{}_Prediction_data.csv".format(a))
            
    return data_pre_all,outbreak_before,outbreak_after
