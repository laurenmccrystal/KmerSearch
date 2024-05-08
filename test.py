
from K-mer.py import *
from ReadingFile Kmer.py import *

def test_list_kmers():
   list_nucleotides = "ATGTCTGTCTGAA"
   k = 2
   assert list_kmers(list_nucleotides, k) == ['AT', 'TG', 'GT', 'TC', 'CT', 'TG', 'GT', 'TC', 'CT', 'TG', 'GA', 'AA']

def test_list_kmer_letter():
  with pytest.raises(ValueError):
  isPrime('B', 'D', 'E', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U', 'V', 'W', 'X', 'Y', 'Z') == False
 
def test_list_kmer_longer():
  list_nucleotides = "ATGTCTGTCTGAATCGATCGATCGA"
  k = 4
  assert list_kmers(list_nucleotides, k) == ['ATGT', 'TGTC', 'GTCT', 'TCTG', 'CTGT', 'TGTC', 'GTCG', 'TCGA', 'CGAT', 'GATC', 'ATCG', 'TCGA'] == True
  
def test_list_kmer_shorter():
  list_nucleotides = "TT"
  k = 3
  assert list_kmers(list_nucleotides, k) == False
  
def test_list_kmer_space():
  list_nucleotides = " "
  assert list_kmers(list_nucleotides, k) == False
  
def test_list_kmer_nothing():
  list_nucleotides = ""
  assert list_kmers(list_nucleotides, k) == False
  
def test_list_kmer_diff_letters():
  list_nucleotides = "JKDJKSPOEM"
  k = 2
  assert list_kmers(list_nucleotides, k) == False
  
def test_list_kmer_space():
  list_nucleotides = "AT"
  k = 3
  assert list_kmers(list_nucleotides, k) == False

###############################################################################################################################################################################

def unique_list_nucleotides():
  unique_list_nucleotides = "ATGTCTGTCTGAA"
  k = 2
  assert unique_list_kmers(unique_list_nucleotides, k) == True 

def unique_list_nucleotides_nothing():
  unique_list_nucleotides = ""
  k = 2
  assert unique_list_kmers(unique_list_nucleotides, k) == False
  
def unique_list_nucleotides_no_k():
  unique_list_nucleotides = "ATGTCTGTCTGAA"
  k = 0
  assert unique_list_kmers(unique_list_nucleotides, k) == False
  
def unique_list_nucleotides():
  unique_list_nucleotides = "AT"
  k = 3
  assert unique_list_kmers(unique_list_nucleotides, k) == False
  
def unique_list_nucleotides():
  unique_list_nucleotides = "ATGTCTGTCTGAA"
  k = 2
  assert unique_list_kmers(unique_list_nucleotides, k) == True 
  
def unique_list_nucleotides():
  unique_list_nucleotides = "ATGGTTATCCTGA"
  k = 3
  assert unique_list_kmers(unique_list_nucleotides, k) == True  
 
def test_list_kmer_letter():
  with pytest.raises(ValueError):
  isPrime('B', 'D', 'E', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U', 'V', 'W', 'X', 'Y', 'Z') == False

#####################################################################################################################################################################

def test_list_kmer_typical_example():
  DNA_sequence = "ATGTCTGTCTGAA"
  k = 2
  assert list_kmers(DNA_sequence, k) == True 
  
def test_list_kmer_nothing():
  DNA_sequence = " "
  k = 2
  assert list_kmers(DNA_sequence, k) == False 

def test_list_kmer_no_space():
  DNA_sequence = ""
  k = 1
  assert list_kmers(DNA_sequence, k) == False 

def test_list_kmer_wrong_letters():
  DNA_sequence = "nfdjfbdsjhbgdsh"
  k = 3
  assert list_kmers(DNA_sequence, k) == False
  
def test_list_kmer_no_space():
  DNA_sequence = "ATCTA"
  k = 7
  assert list_kmers(DNA_sequence, k) == False 
  

#####################################################################################################################################################################

def read_file_typical():
  filename = "'../shared/439539/reads.fa'"
  assert read_file(filename) == True 

def read_file_example():
  filename = "nhvhjfukfcf"
  assert read_file(filename) == False
  
def read_file_no_space():
  filename = ""
  assert read_file(filename) == False 

def read_file_space():
  filename = " "
  assert read_file(filename) == False

#####################################################################################################################################################################

def test_smallest_k_value_wrong():
  DNA_sequence = ""
  assert smallest_k_value(DNA_sequence) == False 

def test_smallest_k_value_space():
  DNA_sequence = " "
  assert smallest_k_value(DNA_sequence) == False

def test_smallest_k_value_wrong_letters():
  DNA_sequence = "fjdnsjkgbsg"
  assert smallest_k_value(DNA_sequence) == False
  
def test_smallest_k_value_number():
  DNA_sequence = "654387465AT"
  assert smallest_k_value(DNA_sequence) == False
  
def test_smallest_k_value(2):
  DNA_sequence = "ATA"
  assert smallest_k_value(DNA_sequence) == True
  
def test_smallest_k_value(5):
  DNA_sequence = "AAAAAA"
  assert smallest_k_value(DNA_sequence) == True
  











 
