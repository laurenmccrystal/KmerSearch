#!/usr/bin/env python3 #make sure it runs python 3 

#Question 2 

def list_kmers(DNA_sequence, k): #this takes the DNA sequence from the file and the k = 2 value to give a dictionary matching this criteria 
    """
    This function generates a dictionary of unique kmers from the uploaded file DNA_sequence
  
    Arguments: 
      DNA_sequence (string): This string is from a file with a dataset that contains a list of nucleotides 
      k (integer): k represents the number of nucleotide bases in the kmer
  
    Return: 
      Dict: A new dictionary is created which outputs all unique kmers and their unique subsequent kmers from the list of nucleotides
    """
    substring_dict = {} #this creates an empty dictionary that stores the information from DNA_sequence and k
    for i in range(len(DNA_sequence) - k + 1): # this makes a loop by searching through the DNA_sequence file using the k value
        substring = DNA_sequence[i:i+k] #this stores the kmer in the DNA_sequence
        if substring not in substring_dict: #this checks if the kmer found in the loop is in the dictionary and if it is not in the list it gets added
            substring_dict[substring] = set() #continuation of the kmer being added to the list if it was not already added
        if i+k < len(DNA_sequence): #this checks to see if the subsequent kmer is in the list, and if it is not it gets added to the dictionary
            substring_dict[substring].add(DNA_sequence[i+1:i+k+1]) #continuation of the subsequent kmer being added to the dictionary if it is not added already
    return substring_dict #this returns the dictionary using the DNA-sequence file and the k value

def read_file(filename): #this reads the information from the file that was imported
    """
    This function reads the nucleotide sequences and then stores the nucleotide sequences as kmers in a list

    Arguments: 
      filename (string): This is how the data can be loaded from the imported file 
    
    Return:
      list: A list is returned which contains all of the unique kmers and their subsequent kmer sequences
    """
  complete_kmer = [] #this list stores the DNA sequences that the code is being asked to list
  with open(filename, 'r') as file: #this opens the data and reads the information until it has all been run
    complete_sequence = "" #this helps open the data set 
    for line in file: #this creates a loop to go through the file
      if line.startswith(">"): #this information is important because it will skip headers that are not needed and give incorrect information
        if complete_sequence:  #complete sequence appends the sequence and adds it to complete_kmer 
          complete_kmer.append(complete_sequence) #continuation of previous explanation
          complete_sequence = "" #continuation of the previous explanation
      else: #if the line does not contain a > then it contains DNA data that we want to add 
          complete_sequence += line.strip() #this adds wanted data throughout the dataset 
    if complete_sequence: #this checks to make sure that all of the DNA data was added to complete_sequence
        complete_kmer.append(complete_sequence) #append the last sequence to complete_kmer
  return complete_kmer #this returns the complete list that was taken from the file

DNA_sequence = '../shared/439539/reads.fa' #defining the list of nucleotides from a DNA sequence from a particular file
k = 2 #set k to give an output of 2 (kmer size)

complete_kmer = read_file(DNA_sequence) #this takes the information from the file using the DNA_sequence file and stores them in complete_kmer

for sequence in complete_kmer: #this starts a loop for the data that is contained in complete_kmer list
  kmer_dict = list_kmers(sequence, k) #a dictionary is generated containing all of the kmers and their subsquent kmers 
  for kmer in kmer_dict.keys(): # another loop is started to go through each kmer in the dictionary
    subsequent_kmers = kmer_dict[kmer] #this line matches kmers with their possible subsequent kmers 
    print(f"K-mer: {kmer}, Subsequent K-mers: {subsequent_kmers}") #kmers and their subsequent kmers are printed out in the complete_kmer list
    
##################################################################################################################
#!/usr/bin/env python3 #make sure it runs python 3 

#Question 3

DNA_sequence = '../shared/439539/reads.fa'  # defining the path to the DNA sequence file

def smallest_k_value(DNA_sequence): #defining a new function to count the smallest value of k
    """
    This function finds the smallest value of k when every substring only has one subsequent substring

    Arguments: 
    DNA_sequence (string): This is how the data can be loaded from the imported file
    
    Return: 
    Integer: The function outputs the smallest value of k possible out of the entire DNA sequence in the file
    """
    k = 1  # start with k = 1, and increase from there 
    while True: #this starts a loop
        kmer_dict = list_kmers(DNA_sequence, k)  # dictionary called kmer_dict is generated using the file and the defined value of k
        if all(len(subsequent_kmers) == 1 for subsequent_kmers in kmer_dict.values()): #this checks every line for whatever the k value is set to, including kmer and subsequent kmer length
            return k #this returns the value of k 
        k += 1 #one is added to the loop every time through until we get the smallest value of k where every substring has only one possible substring that follows it 
smallest_value_of_k = smallest_k_value(DNA_sequence) #this allows us to find the smallest substring of k 
print("This is the smallest k value where every substring has only one possible substring that follows it:", smallest_value_of_k) #this displays what we want as text

    
  
