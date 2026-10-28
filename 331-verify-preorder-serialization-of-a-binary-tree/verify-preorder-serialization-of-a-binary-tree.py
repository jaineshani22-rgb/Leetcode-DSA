class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        
        for node in preorder.split(','):
            # Each node consumes 1 slot
            slots -= 1
            
            # If slots drop below 0, we have too many nodes for the tree structure
            if slots < 0:
                return False
                
            # If the node is not a null node '#', it creates 2 new child slots
            if node != '#':
                slots += 2
                
        # Valid if all slots are fully accounted for (0 remaining)
        return slots == 0