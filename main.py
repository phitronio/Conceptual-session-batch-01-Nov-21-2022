import pandas as pd
import numpy as np
import csv
import time

data = {
  "Outlook": ["Rainy", "Rainy", "Overcast","Sunny","Sunny","Sunny","Overcast","Rainy","Rainy","Sunny","Rainy","Overcast","Overcast","Sunny"],
  "Temp": ["Hot","Hot","Hot","Mild","Cool","Cool","Cool","Mild","Cool","Mild","Mild","Mild","Hot","Mild"],
  "Humidity": ["High", "High", "High","High","Normal","Normal","Normal","High","Normal","Normal","Normal","High","Normal","High"],
  "Windy":['no','yes','no','no','no','yes','yes','no','no','no','yes','yes','no','yes'],
  "Play":["no","no","yes","yes","yes","no","yes","no","yes","yes","yes","yes","yes","no"]
}

df = pd.DataFrame(data)
# processing
x=df.drop(df.columns[-1],axis=1)
y=df[df.columns[-1]]

# Model training 
dct={}
totalData=len(y)
totalYes=0
for item in y:
    if item == "yes":
        totalYes+=1
for item in x.columns:
    uniqueList = np.unique(df[item])
    for feature in uniqueList:
        cnt=0
        cntYes=0
        for indx in range(len(df[item])):
            if feature == df[item][indx] and y[indx]=="yes":
                cntYes+=1
            if feature == df[item][indx]:
                cnt+=1
        dct[feature]={"yes": cntYes,"no":cnt-cntYes,"total": cnt}

# Testing 
test = ["Rainy","Hot","Normal","yes"]
sum1Yes=(totalYes/totalData)
sum2Yes=1
for feature in test:
    sum1Yes*=(dct[feature]["yes"]/totalYes)
    sum2Yes*=(dct[feature]["total"]/totalData)
sumYes=(sum1Yes/sum2Yes)
totalNo=(totalData-totalYes)
sum1No=(totalNo/totalData)
sum2No=1
for feature in test:
    sum1No*=(dct[feature]["no"]/totalNo)
    sum2No*=(dct[feature]["total"]/totalData)
sumNo=(sum1No/sum2No)

print(sumYes,sumNo)





