#!/usr/bin/env python3 #make sure it runs python 3 

list_nucleotides = "ATGTCTGTCTGAA" #defining the list of nucleotides 
k = 2 #set k to give an output of 2

def list_kmers(list_nucleotides, k): #this defines the function to list all of the possible kmers 
  get_kmers = [] #this creates an open list for the kmers to go into 
  for i in range(len(list_nucleotides) - k + 1): #determines the number of iterations needed to find each set of kmer values 
    kmer = list_nucleotides[i:i+k] #this line gets the list of kmers needed by going through the list starting with one nucleotide and ending with another nucleotide + 1
    get_kmers.append(kmer) #this line gets all of the kmers and prints them
  return get_kmers #this line returns all of the possible kmers 

print(list_kmers(list_nucleotides, k)) #this line prints all of the kmers possible 

##############################################################

unique_list_nucleotides = "ATGTCTGTCTGAA" #defining the list of nucleotides 
k = 2 #set k to give an output of 2

def unique_list_kmers(unique_list_nucleotides, k): #this creates a function that outputs only unique kmers from a list
  unique_get_kmers = {} #this makes an empty list to store unique kmers 
  for i in range(len(unique_list_nucleotides) - k + 1): #determines the number of iterations needed to find each set of kmer values 
    unique_kmer = unique_list_nucleotides[i:i+k] #this line gathers kmers based on k, and assigns them to the unique_kmer function
    if unique_kmer not in unique_get_kmers:#this if statement checks to see if the kmer in the loop has already been seen 
      unique_get_kmers.append(unique_kmer) #only if the kmer is not in the list, then it is added to the list
  return unique_get_kmers # this line "returns" all of the unique kmers in the list 

print(unique_list_kmers(unique_list_nucleotides, k)) #this prints the unique kmers 
  
#################################################################################

list_nucleotides = "ATGTCTGTCTGAA" #defining the list of nucleotides 
k = 2 #set k to give an output of 2

def subsequent_list(list_nucleotides, k):
  check_next = []
    for i in range(len(unique_list_nucleotides) - k + 1): #determines the number of iterations needed to find each set of kmer values 
      unique_kmer = unique_list_nucleotides[i:i+k]
      if unique_kmer not in unique_get_kmers:
        unique_get_kmers.append(unique_kmer)
        
      
      #sort by next letter 
      #see if the next letter is unique 
      #if it is unique then add it to the list and go to the next to see if that is still unique 
    
    
  

