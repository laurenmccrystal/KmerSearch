Welcome to the README.md script for this Kmer Search code!

My name is Lauren McCrystal, and I was tasked to with developing Python code to analyze DNA sequences, specifically by searching for k-mer sequences. Each set of code that you will find in this repository is commented and therefore it should be easily reproducable. 

There will be a couple of different files in this repository! In the **K-mer.py file**, you can see how an example DNA sequence was taken and tested to verify that it outputs all k-mers using the function list_kmers. Additionally, this code was further manipulated to output unique kmers in the example DNA sequnce which is defined as the function unique_list_kmers. In this unique list of kmers from the example data, I also includes a list of unique subsequent kmers because genome assembly is constructed utilizing kmer substrings. 

Another file that you will find in this repository us called **ReadingFileKmer.py**. This code reads a specific file (reads.fa) containing DNA sequences. The following code was developed to identify all possible kmers, and additionally all possible subsequent kmers. 
In the same file, there is another section of code for Question 3, which identifies the value of k where every substring has only one possible substring that follows it. The function called smallest_k_value identifies the smallest value using the previous functions. 

Laslty, you will notice a file called **test.py**. This file has been created to make sure that no matter what the input is for the defined functions, it should run as expected without error. Feel free to use your own tests, or the ones from this file. 
