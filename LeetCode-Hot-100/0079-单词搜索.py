class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y, now, visited):
            # 当前格子已经匹配 word[now]
            if now == len(word) - 1:
                return True

            for dx, dy in direct:
                new_x = x + dx
                new_y = y + dy

                if (
                    0 <= new_x < m
                    and 0 <= new_y < n
                    and (new_x, new_y) not in visited
                    and board[new_x][new_y] == word[now + 1]
                ):
                    # 创建新的集合，不修改当前 visited
                    new_visited = visited | {(new_x, new_y)}

                    if dfs(new_x, new_y, now + 1, new_visited):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, {(i, j)}):
                        return True

        return False
