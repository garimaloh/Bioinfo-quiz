#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:20:30 2019

@author: GARIMA
"""
#part2-----------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

fn =sys.argv[1]
f1=sys.argv[2]
f2=sys.argv[3]
f3=sys.argv[4]

cons=int(sys.argv[5])
def readfile(file):
 f=open (file)
 f.readline()
 c=0
 r=0
 fcov= {}
 for line in f:
  line = line.strip()
     
  data = line.split("\t")
  r=r+1
  cov =int( data[3]) # column 4
  if (cov>cons) : 
   c=c+1
 return (c/r)
fc0=readfile(fn)
fc1=readfile(f1)
fc2=readfile(f2)
fc3=readfile(f3)

fcov={0:fc0 , 1:fc1, 2:fc2 , 3:fc3}
print(fcov)  

w = csv.writer(open("fc.csv", "w"))

for keys, value in fcov.items():
  w.writerow([keys, value]) 
 
 
# part3---------------------------------------------------------------------------------------------------

fw=plt.figure(figsize=(50,30))
ax = fw.add_subplot(1, 1, 1)

ax.tick_params(labelsize=20)     # plotting bar plot

ax.set_xticklabels(fcov.keys(), rotation=90, rotation_mode='anchor')
ax.set_ylabel('Fractional Coverage',fontsize = 40, fontweight = 'bold')
ax.set_xlabel('Samples', fontsize = 40, fontweight = 'bold')
for tick in ax.xaxis.get_major_ticks():
      tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
      tick.label1.set_fontweight('bold')
X = np.arange(len(fcov))
ax = plt.subplot(111)
ax.bar(X,fcov.values(),width=0.2,color='lightgreen',align='center')

plt.xticks(X,fcov.keys())
plt.title('Sequence Alignment', fontsize = 50, fontweight = 'bold') 
plt.show()

fw.savefig("plot.pdf")

readfile(fn)

