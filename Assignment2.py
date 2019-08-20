import numpy as np
import csv
from io import StringIO
import requests

# url="https://sites.google.com/site/chnyyang/price_data.csv"
# r = requests.get(url) 

# with open("price_data.csv", "wb") as code:
	# code.write(r.content)
	
	
file="C:\\Users\\gey5\\Downloads\\price_data.csv"
with open(file,"r") as price_data:
	reader=csv.reader(price_data)
	count=0
	LMT=[]
	AMD=[]
	MSFT=[]
	for line in reader:
		if count!=0:
			LMT.append(float(line[1]))
			AMD.append(float(line[2]))
			MSFT.append(float(line[3]))
		count+=1
returns_LMT=[]
returns_AMD=[]
returns_MSFT=[]
for i in range(len(LMT)-1):
	rt_LMT=(LMT[i+1]-LMT[i])/LMT[i]
	returns_LMT.append(rt_LMT)

for i in range(len(AMD)-1):
	rt_AMD=(AMD[i+1]-AMD[i])/AMD[i]
	returns_AMD.append(rt_AMD)
	
for i in range(len(MSFT)-1):
	rt_MSFT=(MSFT[i+1]-MSFT[i])/MSFT[i]
	returns_MSFT.append(rt_MSFT)

mean_LMT=np.mean(LMT)
mean_AMD=np.mean(AMD)
mean_MSFT=np.mean(MSFT)

covariance_LMT=np.cov(LMT)
covariance_AMD=np.cov(AMD)
covariance_MSFT=np.cov(MSFT)


for i in range(len(LMT)-1):
	print(returns_LMT[i],returns_AMD[i],returns_MSFT[i])
