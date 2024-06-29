# https://leetcode.com/problems/course-schedule/

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for x in range(numCourses)]
        indegree = [0] * numCourses

        for pair in prerequisites:
            edges[pair[1]].append(pair[0])
            indegree[pair[0]] += 1
        
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = 0
        while queue:
            node = queue.pop()
            visited += 1
            for item in edges[node]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    queue.append(item)
        
        return numCourses == visited
    

if __name__ == '__main__':
    sol = Solution()
    sol.canFinish(2, [[0,1]])