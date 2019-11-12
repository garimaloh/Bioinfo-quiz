# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:20:30 2019

@author: GARIMA
"""
#part2-----------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import csv

f =open('sample3.txt')
fcov = {}
f.readline
c=0

cons=int(input("Enter a threshold"))

for line in f:
    line = line.strip()
     
    data = line.split("\t")
   
    cov = data[3] # column 4
    fc=(int(cov)/cons)
    c=c+1
    fcov[c]=fc
f.close()   

w = csv.writer(open("sample3table.csv", "w"))
for keys, value in fcov.items():
    w.writerow([keys, value])
 
# part3---------------------------------------------------------------------------------------------------

fw=plt.figure(figsize=(50,30))
ax = fw.add_subplot(1, 1, 1)

ax.tick_params(labelsize=20)     # plotting bar plot

ax.set_xticklabels(fcov.keys(), rotation=90, rotation_mode='anchor')
ax.set_ylabel('Fractional Coverage',fontsize = 40, fontweight = 'bold')
ax.set_xlabel('Regions', fontsize = 40, fontweight = 'bold')
for tick in ax.xaxis.get_major_ticks():
      tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
      tick.label1.set_fontweight('bold')
X = np.arange(len(fcov))
ax = plt.subplot(111)
ax.bar(X,fcov.values(),width=0.2,color='lightgreen',align='center')

ax.legend(('Total'))
plt.xticks(X,fcov.keys())
plt.title('Sequence Alignment', fontsize = 50, fontweight = 'bold') 
plt.show()

fw.savefig("C:/Users/GARIMA/.spyder-py3/sample3.pdf")