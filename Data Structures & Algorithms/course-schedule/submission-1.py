class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        myMap = {}
        for course, pre in prerequisites:
            if course not in myMap:
                myMap[course] = []
            myMap[course].append(pre)
        visiting = set()

        for course, pre in prerequisites:
            if not self.dfs(course, myMap, visiting):
                return False
        return True
        
    
    def dfs(self, course, myMap, visiting):
        if course in visiting:
            return False
        if course not in myMap:
            return True
        
        visiting.add(course)
        for pre in myMap[course]:
            if not self.dfs(pre, myMap, visiting):
                return False
        
        visiting.remove(course)
        del myMap[course]
        return True