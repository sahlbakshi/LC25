class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adjacency_list = {}
        for i in range(numCourses):
            adjacency_list[i] = []
        
        for prerequisite, course in prerequisites:
            adjacency_list[course].append(prerequisite)

        visiting = set()
        visited = set()
        
        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True

            visiting.add(course)

            course_prerequisites = adjacency_list[course]
            for prerequisite in course_prerequisites:
                if not dfs(prerequisite):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if course not in visited and not dfs(course):
                return False
        
        return True
