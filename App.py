import statistics
import csv
#import plotly.figure_factory as ff
import pandas as pd
df=pd.read_csv("height-weight.csv")
heightList=df["Height(Inches)"].to_list()
weightList=df["Weight(Pounds)"].to_list()
hMean=statistics.mean(heightList)
wMean=statistics.mean(weightList)
hMedian=statistics.median(heightList)
wMedian=statistics.median(weightList)
hMode=statistics.mode(heightList)
wMode=statistics.mode(weightList)
hstdev=statistics.stdev(heightList)
wstdev=statistics.stdev(weightList)
print("mean,median,mode of height{},{},{}",format(hMean,hMedian,hMode)
print("mean,median,mode of weight{},{},{}",format(wMean,wMedian,wMode)
height1stdevs,height1stdeve=hMean-hstdev,hMean+hstdev
height2stdevs,height2stdeve=hMean-2*hstdev,hMean+2*hstdev
height3stdevs,height3stdeve=hMean-3*hstdev,hMean+3*hstdev
weight1stdevs,weight1stdeve=wMean-wstdev,wMean+wstdev
weight2stdevs,weight2stdeve=wMean-2*wstdev,wMean+2*wstdev
weight3stdevs,weight3stdeve=wMean-3*wstdev,wMean+3*wstdev

hList1stdev=[result for result in heightList if result>height1stdevs and result<height1stdeve]
hList2stdev=[result for result in heightList if result>height2stdevs and result<height2stdeve]
hList3stdev=[result for result in heightList if result>height3stdevs and result<height3stdeve]
wList1stdev=[result for result in weightList if result>weight1stdevs and result<weight1stdeve]
wList2stdev=[result for result in weightList if result>weight2stdevs and result<weight2stdeve]
wList3stdev=[result for result in weightList if result>weight3stdevs and result<weight3stdeve]
print("{}% of data for height lies within 1st standard deviation",format(len(hList1stdev)*100.0/len(heightList)))
print("{}% of data for height lies within 2nd standard deviation",format(len(hList2stdev)*100.0/len(heightList)))
print("{}% of data for height lies within 3rd standard deviation",format(len(hList3stdev)*100.0/len(heightList)))
print("{}% of data for weight lies within 1st standard deviation",format(len(wList1stdev)*100.0/len(weightList)))
print("{}% of data for weight lies within 2nd standard deviation",format(len(wList2stdev)*100.0/len(weightList)))
print("{}% of data for weight lies within 3rd standard deviation",format(len(wList3stdev)*100.0/len(weightList)))    
