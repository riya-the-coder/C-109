import statistics
import random
import csv
import plotly.figure_factory as ff
import pandas as pd
diceResult=[]
for i in range(0,1000):
	dice1=random.randint(1,6)
	dice2=random.randint(1,6)
	diceResult.append(dice1+dice2)
mean=sum(diceResult)/len(diceResult)
stdev=statistics.stdev(diceResult)
median=statistics.median(diceResult)
mode=statistics.mode(diceResult)
print(mean)
print(stdev)
print(median)
print(mode)
fig=ff.create_distplot([diceResult],["result"],show_hist=False)
fig.show()
