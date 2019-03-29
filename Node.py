class Node:
    def __init__(self, n, d, label, l, r):
        self.name = [n]
        self.distance = d
        self.label = label
        self.left = l
        self.right = r

    def setDistance(self, d):
        self.distance = d

    def setLabel(self, l):
        self.label = l

    #  determine two cluster, i, j where distance is smallest

    # if multiple of same number, say that there are multiple optimum trees

    # define new cluster k, ck = ci U cj
    # define dkl for all l by formula
    # dkl = dil*ci_djl*cj/ci+cj
    # define new nodes for daughters i, j, place at height: dij/2
    # dij = 1/ci*cj*sum of distances
    # add k to current clusters and remove i, j

    # terminate when only two cluster i, j, remain
    # place root at height dij/2
