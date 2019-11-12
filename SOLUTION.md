
# DZD Comp Bio Candidate Quiz 

## Solutions 

[  Please provide the command to invoke the script that reproduces the below solutions here.  ] 

-Q1----------------------------------------------------------------------------------------------------------------------------------------------------------------------
$ bowtie2-build sample/mecA.fa sample/index   #buid index

$ bowtie2 -x ~/miniconda3/sample/index -1 sample0.1.fastq  -2 sample0.2.fastq > sample0.sam   #apply bowtie2
$ bowtie2 -x ~/miniconda3/sample/index -1 sample1.1.fastq  -2 sample1.2.fastq > sample1.sam
$ bowtie2 -x ~/miniconda3/sample/index -1 sample2.1.fastq  -2 sample2.2.fastq > sample2.sam
$ bowtie2 -x ~/miniconda3/sample/index -1 sample3.1.fastq  -2 sample3.2.fastq > sample3.sam

$ samtools view -bS sample0.sam > sample0.bam   #convertt SAM to BAM
$ samtools view -bS sample1.sam > sample1.bam   #BAM files are in folder Q1 bam_files
$ samtools view -bS sample2.sam > sample2.bam
$ samtools view -bS sample3.sam > sample3.bam

$ bedtools genomecov -ibam sample0.bam -bg > sample0.bedgraph # get bedgraph from BAM using genomecov and bedgrapgh are in folder Q2 bedgraph
$ bedtools genomecov -ibam sample1.bam -bg > sample1.bedgraph
$ bedtools genomecov -ibam sample2.bam -bg > sample2.bedgraph
$ bedtools genomecov -ibam sample3.bam -bg > sample3.bedgraph

Alternatee solution--------------------------------------------------------------------------------------------------------------------------------------------------
#! /usr/bin/env bash                       #automated script in bash to perform above tasks
for filename in  sample*.1.fastq 
  do
   file=${filename:0:7} 
   bowtie2 -x ~/miniconda3/sample/index -1 "$file.1.fastq" -2 "$file.2.fastq"  > "$file".sam 
   samtools view -bS "$file".sam > "$file".bam
   bedtools genomecov -ibam "$file".bam -bg > "$file".bedgraph 
   echo "$filename","$file.2.fastq"
   echo "$file"
  done;

#Q2---------------------------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import csv

f =open('sample3.txt')
fcov = {}
f.readline
c=0

cons=int(input("Enter a threshold"))          #user specified threshold

for line in f:
    line = line.strip()
     
    data = line.split("\t")
   
    cov = data[3] # column 4 
    fc=(int(cov)/cons)                      #fractional coverage                 
    c=c+1
    fcov[c]=fc
f.close()   

w = csv.writer(open("sample3table.csv", "w")) #saving table to csv
for keys, value in fcov.items():
    w.writerow([keys, value])
 
#Q3----------------------------------------------------------------------------------------------------------------------------------------------------------

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

fw.savefig("C:/Users/GARIMA/.spyder-py3/sample3.pdf")  #visualize fractional coverage saved to pdf
  
  <br>

#### 1. Alignment   

[  If you have reasons for using the aligner that you've used, please provide them here.  ]

I have used bowtie2 becuase it has more information on SAM file than BWA (Burrows Wheeler Algorithm).It contains more tags and information.
<br> 

#### 2. Fractional Coverage 

[  Please list the fractional coverages for each sample here. If this lives in a file, just specify the 
path.  ]

Frational coverage for each sample are in folder Q2 fractional cov table and bedgraph are in Q2 bed graph


<br> 


#### 3. Visualizing Fractional Coverage (Bonus)

[  Please include the resulting plot here. You can include images in `markdown` like 
`!(image_name)[/path/to/image]`.  ]

The bar plot are in folder Q3 plots	for each sample in pdf
