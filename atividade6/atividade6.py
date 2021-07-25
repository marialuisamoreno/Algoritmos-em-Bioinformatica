# Based on https://www.programmersought.com/article/2659422187/
# Modified by Maria luisa Santos Moreno Sanches

import numpy as np

def backtracking(path, S, value, result, seq1, seq2):
    if value != []:
        key = value[0]
        result.append(key)
        value = path[key]
        i = int((key.split(',')[0]).strip('['))
        j = int((key.split(',')[1]).strip(']'))
    if S[i, j] == 0:
        x = 0
        y = 0
        s1 = ''
        s2 = ''
        md = ''
        score_values = ''
        score_sign = ''
        for n in range(len(result)-2, -1, -1):
            point = result[n]
            i = int((point.split(',')[0]).strip('['))
            j = int((point.split(',')[1]).strip(']'))
            # Editing to print 
            if S[i][j] > 9: 
                score_values += str(S[i][j]) + ' '
                score_sign += '+  '
            else: 
                if S[i][j] < -9:
                    score_values += str(S[i][j]) + ' '
                    score_sign += '-  '
                elif S[i][j] > 0: 
                    score_values += str(S[i][j]) + '  '
                    score_sign += '+  '
                else: 
                    score_values += str(S[i][j]) + '  '
                    score_sign += '-  '
            if i == x:
                s1 += '-  '
                s2 += seq2[j-1] + '  '
                md += '   '
            elif j == y:
                s1 += seq1[i-1] + '  '
                s2 += '-  '
                md += '   '
            else:
                s1 += seq1[i-1] + '  '
                s2 += seq2[j-1] + '  '
                md += '|  '
            x = i
            y = j
        
        print('\nAlinhamento:')
        print('s1: %s'%s1)
        print('    '+md)
        print('s2: %s'%s2)
        print('sg: ' + score_sign)
        print('sc: ' + score_values)
    else:
        backtracking(path, S, value, result, seq1, seq2)

def Smith_Waterman(seq1, seq2, mS, mmS, w1):
    path = {}
    S = np.zeros([len(seq1) + 1, len(seq2) + 1], int)

    for i in range(0, len(seq1) + 1):
        for j in range(0, len(seq2) + 1):
            if i == 0 or j == 0:
                path['[' + str(i) + ', ' + str(j) + ']'] = []
            else:
                if seq1[i - 1] == seq2[j - 1]:
                    s = mS
                else:
                    s = mmS
                L = S[i - 1, j - 1] + s
                P = S[i - 1, j] + w1
                Q = S[i, j - 1] + w1
                S[i, j] = max(L, P, Q, 0)
                path['[' + str(i) + ', ' + str(j) + ']'] = []
                if L == S[i, j]:
                    path['[' + str(i) + ', ' + str(j) + ']'].append('[' + str(i - 1) + ', ' + str(j - 1) + ']')
                if P == S[i, j]:
                    path['[' + str(i) + ', ' + str(j) + ']'].append('[' + str(i - 1) + ', ' + str(j) + ']')
                if Q == S[i, j]:
                    path['[' + str(i) + ', ' + str(j) + ']'].append('[' + str(i) + ', ' + str(j - 1) + ']')

    print("S = \n", S)
    end = np.argwhere(S == S.max())
    for i in end:
        key = str(list(i))
        value = path[key]
        result = [key]
        backtracking(path, S, value, result, seq1, seq2)

# Início do algoritmo
seq1 = "GAATTCAGTTA"
seq2 = "GGATCGA"

Smith_Waterman(seq1, seq2, 5, -3, -4)
