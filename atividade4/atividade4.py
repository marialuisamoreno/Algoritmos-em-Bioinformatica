# Developed by Maria Luisa Santos Moreno Sanches
# Commands from https://biopython.org/

# All files in entrada/ directory will be used
from os import listdir
from os.path import isfile, join
path = 'entrada/'
files = [f for f in listdir(path) if isfile(join(path, f))]

# Import parts of Biopython
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

reads = []
# For each file in the directory
for file in files:
    # File path to your FASTA file
    path_to_file = 'entrada/' + str(file)
    # Open file with "with" statement to avoid problems with access 
    # to original file (in case computer hangs or there will be any other problem)
    with open(path_to_file, mode='r') as handle:
        # Use Biopython's parse function to process individual
        # FASTA records (thus reducing memory footprint)
        for record in SeqIO.parse(handle, 'fasta'):
            # Get all the sequences on a string array
            reads.append(str(record.seq))

# for each substring (big->small) find in the match
def subString(s, n, word):
    for len in range(n, 0, -1):
        substring = s[0: len]
        if (word.find(substring) != -1):
            return s[len: n]
 
# contig string for the result
contig = reads[0]
for r in range(1, len(reads)):
    # this function will return the other half of the string where they don't match
    value = subString(reads[r], len(reads[r]), contig)
    # here will be built the contig
    contig += value

# print(contig)
# Now the contig needs to be saved on a fasta file
exit_file = "saida/contig.fasta"
my_seqs = SeqRecord(Seq(contig), id = "Contig")
saved_file = SeqIO.write(my_seqs, exit_file, 'fasta')

# Checking if everything went okay
if saved_file!=1: print('Error while writing sequence!')