# Sarah Pell
# UPGMA Algorithm


# read input file
fileName = raw_input("What is the name of your input file: ")
f = open(fileName, 'r')

seqNames = []
sequences = []
nameCt = 1
seqCt = 0
for line in f:
    if line[0] == '>':
        seqName = "S" + str(nameCt)
        seqNames.append(seqName)
        nameCt += 1

    else:
        sequences.append(line.rstrip('\n'))
        seqCt += 1
f.close()

# for i in range(len(seqNames)):
#     print(seqNames[i], sequences[i])
# print len(sequences)
# write pairwise distance matrix for all sequences
# distMatrix = [len(sequences)][len(sequences)]
distMatrix = [[0 for x in range(len(sequences)+1)] for y in range(len(sequences)+1)]

distMatrix[0][0] = '-'
for i in range(1, len(seqNames)+1):
    distMatrix[i][0] = seqNames[i-1]
    distMatrix[0][i] = seqNames[i-1]
#
# for k in range(len(seqNames)+1):
#     print distMatrix[k][0]
#     print distMatrix[0][k]


def diffCt(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count


for x in range(1, len(sequences)+1):
    for y in range(1, len(sequences)+1):
        seq1 = sequences[x-1]
        seq2 = sequences[y-1]
        distMatrix[x][y] = diffCt(seq1, seq2)

for h in range(len(sequences)+1):
    for z in range(len(sequences)+1):
        if z == len(sequences):
            print distMatrix[h][z]
        else:
            print distMatrix[h][z],
# go through each sequence and compare letters
