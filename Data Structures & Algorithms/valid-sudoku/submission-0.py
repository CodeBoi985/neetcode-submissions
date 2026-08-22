class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = 9
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        grid = collections.defaultdict(set) # key = (r // 3, c // 3)

        for r in range(digits):
            for c in range(digits):
                value = board[r][c]
                #skip if empty
                if value == ".":
                    continue
                
                #check for duplicates
                if(value in rows[r] or value in columns[c] or value in grid[(r //3, 
                c //3 )]):
                    return False
                
                #add value to the set
                rows[r].add(value)
                columns[c].add(value)
                grid[(r // 3, c // 3)].add(value)
        return True