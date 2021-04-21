# Developed by Maria Luisa Santos Moreno Sanches
# Based on https://www.biostars.org/p/250123/
# Commands from https://biopython.org/

# All files in entrada/ directory will be used
from os import listdir
from os.path import isfile, join
path = 'entrada/'
files = [f for f in listdir(path) if isfile(join(path, f))]

# Import parts of Biopython
from Bio import SeqIO
from Bio.Seq import Seq

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
            # Extract individual parts of the FASTA record
            identifier = record.id
            description = record.description
            sequence = record.seq

            # Example: adapt to extract features you are interested in
            print('\n----------------------------------------------------------')
            print('File: ' + file + '\n')
            print('Processing the record {}:'.format(identifier))
            print('Its description is: {}'.format(description))
            amount_of_nucleotides = len(sequence)
            print('Its sequence contains {} nucleotides, which:'.format(amount_of_nucleotides))
            print('A: {}'.format(sequence.count("A")))
            print('C: {}'.format(sequence.count("C")))
            print('G: {}'.format(sequence.count("G")))
            print('T: {}'.format(sequence.count("T")))
            
