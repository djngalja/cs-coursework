from collections import deque

def bfs(matrix: list[list[int]], i_start: int, j_start: int) -> None:
    queue = deque([(i_start, j_start)])
    matrix[i_start][j_start] = 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        i, j = queue.popleft()
        for i_dir, j_dir in dirs:
            i_new, j_new = i + i_dir, j + j_dir
            if (0 <= i_new < len(matrix) 
                and 0 <= j_new < len(matrix[0]) 
                and matrix[i_new][j_new] == 1):
                matrix[i_new][j_new] = 0
                queue.append((i_new, j_new))

def cnt_shapes(matrix: list[list[int]]) -> tuple[int, int]:
    squares: int = 0
    circles: int = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                if (j == 0 or matrix[i+1][j-1] == 0):
                    squares += 1
                else:
                    circles += 1
                bfs(matrix, i, j)
    return (squares, circles)
                
def main() -> None:
    with open("input.txt", "r") as file:
        matrix = [[int(num) for num in line.split()] for line in file]
    print(*cnt_shapes(matrix))

if __name__ == "__main__":
    main()