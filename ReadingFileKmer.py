#################################################################################
#Question 2 

DNA_sequence = '../shared/439539/reads.fa' #defining the list of nucleotides from a DNA sequence from a particular file
k = 2 #set k to give an output of 2 (kmer size)

def list_kmers(DNA_sequence, k): #this takes the DNA sequence from the file and the k = 2 value to give a dictionary matching this criteria 
    substring_dict = {} #this creates an empty dictionary that stores the information from DNA_sequence and k
    for i in range(len(DNA_sequence) - k + 1): # this makes a loop by searching through the DNA_sequence file using the k value
        substring = DNA_sequence[i:i+k] #this stores the kmer in the DNA_sequence
        if substring not in substring_dict: #this checks if the kmer found in the loop is in the dictionary and if it is not in the list it gets added
            substring_dict[substring] = set() #continuation of the kmer being added to the list if it was not already added
        if i+k < len(DNA_sequence): #this checks to see if the subsequent kmer is in the list, and if it is not it gets added to the dictionary
            substring_dict[substring].add(DNA_sequence[i+1:i+k+1]) #continuation of the subsequent kmer being added to the dictionary if it is not added already
    return substring_dict #this returns the dictionary using the DNA-sequence file and the k value

def read_file(filename): #this reads the information from the file that was imported
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

complete_kmer = read_file(DNA_sequence) #this takes the information from the file using the DNA_sequence file and stores them in complete_kmer

for sequence in complete_kmer: #this starts a loop for the data that is contained in complete_kmer list
  kmer_dict = list_kmers(sequence, k) #a dictionary is generated containing all of the kmers and their subsquent kmers 
  for kmer in kmer_dict.keys(): # another loop is started to go through each kmer in the dictionary
    subsequent_kmers = kmer_dict[kmer] #this line matches kmers with their possible subsequent kmers 
    print(f"K-mer: {kmer}, Subsequent K-mers: {subsequent_kmers}") #kmers and their subsequent kmers are printed out in the complete_kmer list


  

