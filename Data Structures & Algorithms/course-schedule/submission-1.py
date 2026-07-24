class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = {i : [] for i in range(numCourses)}
        for course, preq in prerequisites:
            preqs[course].append(preq)
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if preqs[course] == []:
                return True
            visiting.add(course)
            for preq in preqs[course]:
                if dfs(preq) == False:
                    return False
            visiting.remove(course)
            preqs[course] = []
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True
        
        