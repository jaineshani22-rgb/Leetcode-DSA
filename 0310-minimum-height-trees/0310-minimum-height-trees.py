class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 2:
            return [i for i in range(n)]
            
        # Step 1: Build adjacency list and track degrees
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
        # Step 2: Initialize queue with initial leaves (degree == 1)
        leaves = deque([i for i in range(n) if len(adj[i]) == 1])
        
        # Step 3: Trim leaves layer by layer until 2 or fewer nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count
            
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                # Remove the leaf from its single neighbor
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                
                # If neighbor becomes a new leaf, add it to the queue
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)
                    
        return list(leaves)