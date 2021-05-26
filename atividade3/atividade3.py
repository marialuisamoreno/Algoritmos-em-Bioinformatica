# Developed by Maria Luisa Santos Moreno Sanches
# Commands from https://biopython.org/

# Reference information for Melting Temperature
# http://www.biology.arizona.edu/biomath/tutorials/Linear/LinearFunctionApplication/DNAmelt.html
# https://biopython.org/docs/1.75/api/Bio.SeqUtils.MeltingTemp.html

# All files in entrada/ directory will be used
from os import listdir
from os.path import isfile, join
path = 'entrada/'
files = [f for f in listdir(path) if isfile(join(path, f))]

# Import parts of Biopython
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp as mt

# Import Mat Plot Library
import matplotlib.pyplot as plt
import mplcursors

# Creating an exit file
exit_file = open('saida.txt', 'w')

# Arrays for the Graphic
TMarizona_values = []
TMwallace_values = []
TMGC_values = []
TMNN_values = []
GC_values = []

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

            # Writing information on the txt exit file
            exit_file.writelines('----------------------------------------------------------\n')
            exit_file.writelines('File: ' + file + '\n')
            exit_file.writelines('Processing the record {}:\n'.format(identifier))
            exit_file.writelines('Its description is: {}\n'.format(description))
            amount_of_nucleotides = len(sequence)
            exit_file.writelines('Its sequence contains {} nucleotides, which:\n'.format(amount_of_nucleotides))
            exit_file.writelines('A: {}\n'.format(sequence.count("A")))
            exit_file.writelines('C: {}\n'.format(sequence.count("C")))
            exit_file.writelines('G: {}\n'.format(sequence.count("G")))
            exit_file.writelines('T: {}\n'.format(sequence.count("T")))
            exit_file.writelines('Amount of GC: {}\n'.format(sequence.count("GC")))
            exit_file.writelines('\nMelting Temperature Values\n')

            # Calculating Melting Temperature
            exit_file.writelines('Tm_Wallace: {}\n'.format('%0.2f' % mt.Tm_Wallace(sequence)))
            exit_file.writelines('Tm_GC: {}\n'.format('%0.2f' % mt.Tm_GC(sequence)))
            exit_file.writelines('Tm_NN: {}\n'.format('%0.2f' % mt.Tm_NN(sequence)))

            # From University of Arizona Formula
            amount_of_GC = sequence.count("GC")
            tm = 64.9 + 0.41*(amount_of_GC/amount_of_nucleotides) - (500/amount_of_nucleotides)
            exit_file.writelines('Arizona\'s: {}\n'.format('%0.2f' % tm))
            exit_file.writelines('\n')

            # Getting information for each graphic
            TMarizona_values.append(tm)
            TMwallace_values.append(mt.Tm_Wallace(sequence))
            TMGC_values.append(mt.Tm_GC(sequence))
            TMNN_values.append(mt.Tm_NN(sequence))
            GC_values.append(amount_of_GC)

exit_file.close()

# Plotting Graphs
# Arizona's Formula
plt.scatter(GC_values, TMarizona_values)
plt.title('Arizona\'s Formula', fontsize=12)
plt.xlabel('% of GC', fontsize=10)
plt.ylabel('Melting Temperature ºC', fontsize=10)
plt.savefig('arizona_values.png')
mplcursors.cursor(hover=True)
plt.figure()

# Rule of thumb
plt.scatter(GC_values, TMwallace_values)
plt.title('Rule of thumb', fontsize=12)
plt.xlabel('% of GC', fontsize=10)
plt.ylabel('Melting Temperature ºC', fontsize=10)
plt.savefig('rule_of_thumb_values.png')
mplcursors.cursor(hover=True)
plt.figure()

# Empirical formulas based on GC content
plt.scatter(GC_values, TMGC_values)
plt.title('Empirical Formulas', fontsize=12)
plt.xlabel('% of GC', fontsize=10)
plt.ylabel('Melting Temperature ºC', fontsize=10)
plt.savefig('empirical_formulas_values.png')
mplcursors.cursor(hover=True)
plt.figure()

# Nearest Neighbor Thermodynamics
plt.scatter(GC_values, TMNN_values)
plt.title('Nearest Neighbor Thermodynamics', fontsize=12)
plt.xlabel('% of GC', fontsize=10)
plt.ylabel('Melting Temperature ºC', fontsize=10)
plt.savefig('nn_values.png')
mplcursors.cursor(hover=True)
plt.figure()

# Show all graphics
plt.show()