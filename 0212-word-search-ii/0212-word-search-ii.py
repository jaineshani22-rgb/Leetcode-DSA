class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build the Trie
        root = TrieNode()
        for w in words:
            curr = root
            for char in w:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = w
            
        rows, cols = len(board), len(board[0])
        res = set()
        
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word:
                res.add(next_node.word)
                
            # Temporarily mark cell as visited
            board[r][c] = '#'
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)
                    
            # Restore the cell
            board[r][c] = char
            
            # Optimization: Prune the Trie node if it has no children left
            if not next_node.children:
                del node.children[char]
                
        # Step 2: Start DFS from every cell on the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
                
        return list(res)