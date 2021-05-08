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
            # Modifying the information to the new FASTA file
            record.description = "___RNA convertido___" + record.description
            # Original sequence
            sequence = record.seq
            # Transcribed sequence
            record.seq = sequence.transcribe()
            # Saving the file in a FASTA file
            exit_file = "saida/rna_convertido_" + str(file)
            saved_file = SeqIO.write(record, exit_file, 'fasta')
            # Checking if everything went okay
            if saved_file!=1: print('Error while writing sequence:  ' + record.id)
            # Printing the amount of nucleotides
            amount_of_nucleotides = len(sequence)
            print(record.description)
            print('Its sequence contains {} nucleotides.'.format(amount_of_nucleotides))