class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x

        def union(a, b):
            root1 = find(a)
            root2 = find(b)
            if root1 == root2:
                return False
            parents[root2] = root1
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
        