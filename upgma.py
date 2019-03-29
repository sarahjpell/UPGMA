# Sarah Pell
# UPGMA Algorithm
from Node import Node


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


def initializeNodes(l, nodes):
    label = ""
    for i in range(l):
        label = "S" + str(i)
        node = Node(i, 0, label, None, None)
        nodes.append(node)


# go through each sequence and compare letters
def compareSeq(distMatrix, sequences):
    for i in range(1, len(distMatrix)):
        for j in range(1, len(distMatrix)):
            seq1 = sequences[i - 1]
            seq2 = sequences[j - 1]
            distMatrix[i][j] = diffCt(seq1, seq2)


# print out matrix
def printMatrix(distMatrix):
    for i in range(len(distMatrix)):
        for j in range(len(distMatrix)):
            if j == len(distMatrix) - 1:
                print distMatrix[i][j]
            else:
                print distMatrix[i][j],


# print out matrix
def printUpdatedMatrix(distMatrix):
    print(len(distMatrix))
    for i in range(len(distMatrix)):
        for j in range(len(distMatrix)):
            if j == len(distMatrix):
                print distMatrix[i][j]
            else:
                print distMatrix[i][j],


def calcDist(x, y, nodes):
    distance = 1 / ((len(nodes[x].name)) * (len(nodes[y].name)))
    return distance


def clusterNodes(x, y, val, nodes):
    # calculate dij
    # if nodes don't have daughters
    if nodes[x].left is None or nodes[y].right is None:
        first = 1 / (len(nodes[x].name) * len(nodes[y].name))
        dij = (first * val) / (len(nodes[x].name) + len(nodes[y].name))
        nodes[x].setDistance(dij)
        nodes[y].setDistance(dij)

        labelLeft = "(S" + str(nodes[x].name) + ":" + str(nodes[x].distance) + ")"
        labelRight = "(S" + str(nodes[y].name) + ":" + str(nodes[y].distance) + ")"

        nodes[x].setLabel(labelLeft)
        nodes[y].setLabel(labelRight)

        name = nodes[x].name + nodes[y].name
        newclusterLabel = "(S" + str(name) + ":" + labelLeft + labelRight + ")"
        newNode = Node(name, dij, newclusterLabel, nodes[x], nodes[y])
        nodes.append(newNode)

        print nodes[x].label, nodes[y].label
        print nodes[-1].label

    # else:
    #     first = 1 / (len(nodes[x].name) * len(nodes[y].name))
    #     d1 = (first * nodes[x].distance) / (len(nodes[x].name) + len(nodes[y].name))
    #     d2 = (first * nodes[y].distance) / (len(nodes[x].name) + len(nodes[y].name))
    #     numerator = d1 * len(nodes[x].name) + d2 * len(nodes[y].name)
    #     denominator = len(nodes[x].name) + len(nodes[y].name)
    #     distance = numerator/denominator
    #     nodes[x].setDistance(d1)
    #     nodes[y].setDistance(d2)
    #
    #     labelLeft = "(S" + str(nodes[x].name) + ":" + str(nodes[x].distance) + ")"
    #     labelRight = "(S" + str(nodes[y].name) + ":" + str(nodes[y].distance) + ")"
    #
    #     nodes[x].setLabel(labelLeft)
    #     nodes[y].setLabel(labelRight)
    #
    #     name = nodes[x].name + nodes[y].name
    #     newclusterLabel = "(S" + str(name) + ":" + labelLeft + labelRight + ")"
    #     newNode = Node(name, distance, newclusterLabel, nodes[x], nodes[y])
    #     nodes.append(newNode)
    #
    #     print nodes[x].label, nodes[y].label
    #     print nodes[-1].label

# find the lowest value in the matrix
def lowestVal(matrix, l, nodes):
    smallest = 999999
    x = -9999
    y = -9999

    for i in range(1, l):
        for j in range(1, l):
            if matrix[i][j] < smallest and matrix[i][j] != 0:
                smallest = int(matrix[i][j])
                x, y = i, j

    clusterNodes(x, y, matrix[x][y], nodes)
    return x, y


def findMult(matrix, l, x, y):
    smallest = distMatrix[x][y]
    count = 0
    multipleOptimumTrees = "nothing"

    for i in range(l):
        for j in range(l):
            if matrix[i][j] == smallest:
                count += 1

    if count > 0:
        multipleOptimumTrees = "YES"
    else:
        multipleOptimumTrees = "NO"

    return multipleOptimumTrees


def updateMatrix(matrix, l, x, y, nodes):
    newMatrix = matrix

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if x == i or y == j or x == j or y == i:
                pass
            else:
                newMatrix[i][j] = matrix[i][j]
    newMatrix[-1][y] = nodes[-1].label
    newMatrix[x][-1] = nodes[-1].label

    newDistances = []

    for node in range(len(newMatrix)):
        first = 1 / (len(nodes[x].name) * len(nodes[y].name))
        d1 = (first * nodes[x].distance) / (len(nodes[x].name) + len(nodes[y].name))
        d2 = (first * nodes[y].distance) / (len(nodes[x].name) + len(nodes[y].name))
        numerator = d1 * len(nodes[x].name) + d2 * len(nodes[y].name)
        denominator = len(nodes[x].name) + len(nodes[y].name)
        newDistances.append(numerator / denominator)

    newDistances.append(0)

    for n in range(len(newMatrix)):
        newMatrix[-1][i] = newDistances[n]
        newMatrix[i][-1] = newDistances[n]

    return newMatrix


# read input file
fileName = raw_input("What is the name of your input file: ")
f = open(fileName, 'r')

seqNames = []
sequences = []
nodes = []
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

distMatrix = [[0 for x in range(len(sequences) + 1)] for y in range(len(sequences) + 1)]
distMatrix = initializeMatrix(distMatrix)
initializeNodes(len(seqNames), nodes)

compareSeq(distMatrix, sequences)
# print out distance matrix
print("Distance Matrix: ")
printMatrix(distMatrix)

### upgma stuff ###
print("Phylogenetic Tree: ")
# locate lowest number in matrix, get index of value
phyloTree = ""

end = 0
time = 1
multiple = ""
# end when cluster length is number of sequences
while end == 0:
    # find lowest value in matrix, cluster sequences
    x, y = lowestVal(distMatrix, len(distMatrix), nodes)
    checkClusterLen = len(nodes[-1].name)
    # check to see if should end loop
    if checkClusterLen == len(distMatrix):
        end = 1
    # are there multiple optimum trees?
    if time == 1:
        multiple = findMult(distMatrix, len(distMatrix), x, y)
        print multiple
        time += 1
    # update matrix
    distMatrix = updateMatrix(distMatrix, len(distMatrix), x, y, nodes)

    # update labels
    # updateLabels(phyloTree, distMatrix, x, y)

print(multiple)
