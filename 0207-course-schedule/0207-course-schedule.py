class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)  # pre must be taken before course
            in_degree[course] += 1
            
        # Step 2: Enqueue all courses with 0 prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed_courses = 0
        
        # Step 3: Process the queue (BFS topological sort)
        while queue:
            curr = queue.popleft()
            completed_courses += 1
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # Step 4: If we completed all courses, there are no cycles
        return completed_courses == numCourses