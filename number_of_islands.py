from typing import List

def numIslands(grid: List[List[str]]) -> int:

    def dfs(i, j):

        # return if there are never islands

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid) \
            or grid[i][j] != '1':
            return

        grid[i,j] = 0

        # Search all directions
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)


    count = 0
    for i in range(len(grid)):
        for j in range(len(len(grid[0]))):

            if grid[i][j] == '1':
                dfs(i,j)
                count += 1

    return count



if __name__ == "__main__":
    
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    numIslands(grid)