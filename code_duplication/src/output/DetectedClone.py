class DetectedClone:
    def __init__(self, value, similarity, nodes):
        """
        Initializes a new detected clone
        given its values and origin nodes.

        Arguments:
            value {string} -- String representation common to all the nodes.
            similarity {float} -- Similarity coefficient in range from 0 to 1,
                                  where 0 means completely different and
                                  1 means the nodes are all exactly equal.
            nodes {list[TreeNode]} -- List of origin nodes.
        """

        self.value = value
        self.similarity = similarity
        self.weight = sum([n.weight for n in nodes])
        self.origins = [n.origin for n in nodes]

    def dict(self):
        return {
            "value": self.value,
            "similarity": self.similarity,
            "weight": self.weight,
            "origins": self.origins
        }
