class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqs = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            preqs[course].append(preq)
        visited = set()
        visiting = set()
        ret = []
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for preq in preqs[course]:
                if dfs(preq) == False:
                    return False
            visiting.remove(course)
            visited.add(course)
            ret.append(course)
            preqs[course] = []
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return ret
        