# Developed by Maria Luisa Santos Moreno Sanches

# Sequencias 1 and 2
seq1 = "GGGCAATATGAA---TTTAAA---GTAGAATACCAAATGATAGAAACAGACTGCCTGA-TTGATCATTTTGATTTTTTAAAGTGTGTA------TAAATTGCTGTTCCTTAATTTGATTA"
seq2 = "GGGCAATATGAAATTTTTAAAGGAGTAGAATACGAAATGATAGACACAGACTGCCTGAATTGAGGATTTTGATTTCTTAAATTGTGTTTCTTTCTAAATTGCTGTTCCTTAATTTTATTA"

# Identidade
identidade = 0

# Escore
escore = 0

# Como ambas são obrigatoriamente do mesmo tamanho
for i in range(len(seq1)):
    # Identidade
    if seq1[i] == seq2[i]: identidade += 1

    # Escore
    if seq1[i] == seq2[i] and seq1[i] != "-" and seq2[i] != "-": escore += 5
    elif (seq1[i] == "C" and seq2[i] == "A") or (seq1[i] == "A" and seq2[i] == "C"): escore += -1
    elif (seq1[i] == "G" and seq2[i] == "A") or (seq1[i] == "A" and seq2[i] == "G"): escore += -2
    elif (seq1[i] == "T" and seq2[i] == "A") or (seq1[i] == "A" and seq2[i] == "T"): escore += -1
    elif (seq1[i] == "-" and seq2[i] == "A") or (seq1[i] == "A" and seq2[i] == "-"): escore += -3
    elif (seq1[i] == "C" and seq2[i] == "G") or (seq1[i] == "G" and seq2[i] == "C"): escore += -3
    elif (seq1[i] == "C" and seq2[i] == "T") or (seq1[i] == "T" and seq2[i] == "C"): escore += -2
    elif (seq1[i] == "-" and seq2[i] == "C") or (seq1[i] == "C" and seq2[i] == "-"): escore += -4
    elif (seq1[i] == "G" and seq2[i] == "T") or (seq1[i] == "T" and seq2[i] == "G"): escore += -2
    elif (seq1[i] == "G" and seq2[i] == "-") or (seq1[i] == "-" and seq2[i] == "G"): escore += -2
    elif (seq1[i] == "T" and seq2[i] == "-") or (seq1[i] == "-" and seq2[i] == "T"): escore += -1

# Cálculo da Identidade Média
id_media = (identidade/len(seq1))*100

# Cálculo do Escore Médio
id_escore = (escore/len(seq1))*100

# Cálculo do Máximo Escore possível
max_escore = 5*len(seq1)

print("Total de nucleotideos: " + str(len(seq1)))
print("Identidade: " + str(identidade))
print("Identidade Média: " + str(id_media) + "%")
print("Escore: " + str(escore))
print("Escore Médio: " + str(round(id_escore, 2)) + "%")
print("Escore Máximo: " + str(max_escore))

# Comparando com BioPython
from Bio import pairwise2
from Bio.Seq import Seq 
from Bio.pairwise2 import format_alignment

seq1_ = Seq(seq1) 
seq2_ = Seq(seq2)

alignments = pairwise2.align.globalxx(seq1_, seq2_)
  
# Mostrando os resultados
for alignment in alignments:
    print(format_alignment(*alignment))