# Sarah Pell
# UPGMA Algorithm


# read input file
fileName = raw_input("What is the name of your input file: ")
f = open(fileName, 'r')

seqNames = []
sequences = []
nameCt = 0
seqCt = 0
for line in f:
    if line[0] == '>':
        seqName = "S" + str(nameCt + 1)
        seqNames.append(int(seqName))
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
distMatrix = [[0 for x in range(len(sequences))] for y in range(len(sequences))]
distMatrix[0][0] = int('-')
for i in range(1, len(sequences)):
    distMatrix[i][0] = seqNames[i]
    distMatrix[0][i] = seqNames[i]


def diffCt(s1, s2):
    pass


for x in range(len(distMatrix)):
    for y in range(len(distMatrix)):
        seq1 = sequences[x]
        seq2 = sequences[y]
        distMatrix[x][y] = diffCt(seq1, seq2)

# go through each sequence and compare letters
