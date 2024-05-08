#!/usr/bin/env python3 #make sure it runs python 3 

#Test and get all of the kmer outputs for the example sequence

list_nucleotides = "ATGTCTGTCTGAA" #defining the list of nucleotides 
k = 2 #set k to give an output of 2

def list_kmers(list_nucleotides, k): #this defines the function to list all of the possible kmers 
  """
  This function generates all of the possible kmers from the sample list of nucleotides. 
  
  Argument: 
    list_nucleotides (string): This string is a dataset that contains a list of nucleotides 
    k (integer): k represents the number of nucleotide bases in the kmer 
  
  Return: 
    list_kmers: This function returns a list containing all of the possible kmers from this sample data
  """
    
  get_kmers = [] #this creates an open list for the kmers to go into 
  for i in range(len(list_nucleotides) - k + 1): #determines the number of iterations needed to find each set of kmer values 
    kmer = list_nucleotides[i:i+k] #this line gets the list of kmers needed by going through the list starting with one nucleotide and ending with another nucleotide + 1
    get_kmers.append(kmer) #this line gets all of the kmers and prints them
  return get_kmers #this line returns all of the possible kmers 

print(list_kmers(list_nucleotides, k)) #this line prints all of the kmers possible 

##############################################################
#Question 1

unique_list_nucleotides = "ATGTCTGTCTGAA" #defining the list of nucleotides 
k = 2 #set k to give an output of 2

def unique_list_kmers(unique_list_nucleotides, k): #this takes the DNA sequence from the file and the k = 2 value to give a dictionary matching this criteria 
  
    """
    This function generates a dictionary to define a list of kmers and their subsequent kmers from the list of nucleotides 
  
    Arguments: 
      unique_list_nucleotides (string): This string is a dataset that contains a list of nucleotides 
      k (integer): k represents the number of nucleotide bases in the kmer
    
    Return:
      Dict: A new dictionary is created which outputs all unique kmers and their unique subsequent kmers from the list of nucleotides
    """   
    substring_dict = {} ##this creates an empty dictionary that stores the information from DNA_sequence and k
    for i in range(len(unique_list_nucleotides) - k + 1):  # this makes a loop by searching through the list of nucleotides example using the k value
        substring = unique_list_nucleotides[i:i+k] #this stores the kmer in the nucleotide list 
        if substring not in substring_dict: #this checks if the kmer found in the loop is in the dictionary and if it is not in the list it gets added
            substring_dict[substring] = set() ##continuation of the kmer being added to the list if it was not already added
        if i+k < len(unique_list_nucleotides): #this checks to see if the subsequent kmer is in the list, and if it is not it gets added to the dictionary
            substring_dict[substring].add(unique_list_nucleotides[i+1:i+k+1]) #continuation of the subsequent kmer being added to the dictionary if it is not added already
    return substring_dict #this returns the dictionary using the example nucleotide sequence and the k value

kmer_dict = unique_list_kmers(unique_list_nucleotides, k) #kmer_dict is created using unique kmer sequences and the k value that was defined above
  
for kmer in kmer_dict.keys(): #another loop is started to go through each kmer in the dictionary
  subsequent_kmers = kmer_dict[kmer] #this line matches kmers with their possible subsequent kmers 
  print(f"K-mer: {kmer}, Subsequent K-mers: {subsequent_kmers}") #kmers and their subsequent kmers are printed out in the complete_kmer list
  
