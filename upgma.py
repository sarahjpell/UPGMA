# Sarah Pell
# UPGMA Algorithm


# count differences in 2 given sequences
def diffCt(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count


def initializeMatrix(distMatrix):
    distMatrix[0][0] = '-'
    for i in range(1, len(seqNames) + 1):
        distMatrix[i][0] = seqNames[i - 1]
        distMatrix[0][i] = seqNames[i - 1]
    return distMatrix


# go through each sequence and compare letters
def compareSeq(distMatrix, sequences):
    for i in range(1, len(sequences) + 1):
        for j in range(1, len(sequences) + 1):
            seq1 = sequences[i - 1]
            seq2 = sequences[j - 1]
            distMatrix[i][j] = diffCt(seq1, seq2)


# print out matrix
def printMatrix(distMatrix, sequences):
    for i in range(len(sequences) + 1):
        for j in range(len(sequences) + 1):
            if j == len(sequences):
                print distMatrix[i][j]
            else:
                print distMatrix[i][j],


# find the lowest value in the matrix
def lowestVal(matrix, l):
    smallest = 999999
    previous = 999999

    for i in range(l):
        for j in range(l):
            if matrix[i][j] < smallest and matrix[i][j] != 0 and smallest != previous:
                smallest = matrix[i][j]
                x, y = i, j

    return x, y


def findMult(matrix, l, x, y):
    smallest = distMatrix[x][y]
    count = 0
    for i in range(l):
        for j in range(l):
            if matrix[i][j] == smallest:
                count += 1

    return count


def updateMatrix(matrix, l, x, y):
    row = []
    col = []
    if y < x :
        x, y = y, x
    # update row
    for i in range(1, x):
        row.append(matrix[x][i] + matrix[y][i]/2)
    matrix[y] = row

    #update column
    for i in range(x+1, y):
        matrix[i][y] = (matrix[i][x]+matrix[y][i])/2

    for i in range(y+1, l):
        matrix[i][x] = (matrix[i][x] + matrix[i][y])/2
        #delete
        del matrix[i][y]
    del matrix[y]


# def findDist(matrix, x, y):
#     return matrix[x][y]


def updateLabels(label, matrix, x, y):
    if y < x :
        x, y = y, x

    left = "(S"+str(x)+":"+str(matrix[x][y]/2)+")"
    right = "(S"+str(y)+":"+str(matrix[x][y]/2)+")"
    label.append("(S"+str(x)+str(y)+":"+str(matrix[x][y])+left+right+")")


# read input file
fileName = raw_input("What is the name of your input file: ")
f = open(fileName, 'r')

seqNames = []
sequences = []
nameCt = 1
seqCt = 0
# put sequence name and sequences into arrays
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
distMatrix = [[0 for x in range(len(sequences) + 1)] for y in range(len(sequences) + 1)]
distMatrix = initializeMatrix(distMatrix)

# print distance matrix at i,0 ; 0,j
# for k in range(len(seqNames)+1):
#     print distMatrix[k][0]
#     print distMatrix[0][k]
compareSeq(distMatrix, sequences)
# print out distance matrix
print("Distance Matrix: ")
printMatrix(distMatrix, sequences)

### upgma stuff ###
print("Phylogenetic Tree: ")
# locate lowest number in matrix, get index of value
phyloTree = ""
while len(seqNames) > 1:
    x, y = lowestVal(distMatrix, len(sequences))
    multiple = findMult(distMatrix, len(sequences), x, y)
    if multiple > 0:
        multipleOptimumTrees = "YES"
    else:
        multipleOptimumTrees = "NO"
    s = 's'+str(x)+str(y)
    print(s)
    # update matrix
    updateMatrix(distMatrix, len(sequences), x, y)

    # update labels
    updateLabels(phyloTree, distMatrix, x, y)
