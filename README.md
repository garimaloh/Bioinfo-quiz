
# DZD Comp Bio Candidate Quiz 


Welcome to the DZD Comp Bio Candidate Quiz! 

This is a short assessment designed to test your bioinformatic and data science skills. We tried to 
make the questions as realistic as possible, in that these are the types of things you may be asked 
to do in this position, but we also hope that you find it fair and not too much to ask (you should 
be able to finish it in 2-6 hours, depending on your skill level).   

Good luck! 

<br>

## Questions 

You are only required to answer the first 2 questions, the final one is a bonus that you can feel 
free to answer or not. 

For the final submission, we ask that all calculations you write be written in `python`. This 
is the main programming language we use at DZD and we want to assess your proficiency. 

We also ask that you contain all computations/ operations in a single script that takes in inputs 
related to each question, and produces some outputs that answer those questions. In other words, we 
should be able to execute this script on the command-line and reproduce your answers from the inputs 
we've provided. This script can be in `python` (preferred), `bash` or some other language you might 
know, we leave it to you to design it how you like. 

(Hint: if you end up using `python` for this script, you can call external bioinformatics tools 
via the `subprocess` module.) 

We also ask for the final submission that you provide your written answers in a file `SOLUTION.md`. 
We've provided a template for this alongside this quiz. 

<br> 

#### 1. Alignment   

For each paired-end Illumina sample provided with this quiz (i.e. `sample_data/sample*.[12].fastq`), 
align reads to the mecA gene (`mecA.fa`). Feel free to use any aligner you like, however, if you think 
there are good reasons to use one aligner over another you should provide those reasons in your 
written answers. 

The inputs for this question are the sample FASTQs and the mecA gene reference, and the outputs
should be BAM files for each sample. 

<br> 

#### 2. Fractional Coverage 

Determine **fractional coverage** for each of the above alignments. We define fractional coverage as
the fraction of reference sequence (here, the mecA gene) covered by reads to depth greater than or 
equal to some user-specified threshold (e.g., 5). The `python` script/ function that executes this 
calculation should take this user-specified threshold in as input. 

The inputs for this question are the bam files produced in question 1. and a user-defined depth 
threshold. The outputs should be some table (either written to a file or to stdout) listing the 
fractional coverage for each sample. 

(Hint: `bedtools` might be a good biofinformatic tool to use for this. Specifically, `genomecov`.)

<br> 


#### 3. Visualizing Fractional Coverage (Bonus)

Here, we would like you to visualize the results of question 2. You should plot the fractional coverage
for each sample in a bar graph, and a nice solution would have all of these bars in the same figure. 

(Hint: Here, we suggest you use `python` libraries `pandas` for reading data into dataframes and 
`matplotlib.pyplot` and/ or `seaborn` for rendering the plots.)

	
