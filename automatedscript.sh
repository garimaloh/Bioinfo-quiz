#! /usr/bin/env bash



for filename in  sample*.1.fastq 
  do
   file=${filename:0:7} 
   bowtie2 -x ~/miniconda3/sample/index -1 "$file.1.fastq" -2 "$file.2.fastq"  > "$file".sam 
   samtools view -bS "$file".sam > "$file".bam
   bedtools genomecov -ibam "$file".bam -bg > "$file".bedgraph 
   echo "$filename","$file.2.fastq"
   echo "$file"
  done;
