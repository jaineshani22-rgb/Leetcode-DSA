class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
            
        itinerary = []
        
        def dfs(airport: str):
            # Visit all outgoing edges
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            # Add to itinerary once all outgoing flights from this airport are exhausted
            itinerary.append(airport)
            
        dfs("JFK")
        
        # Reverse the post-order traversal to get the correct chronological path
        return itinerary[::-1]