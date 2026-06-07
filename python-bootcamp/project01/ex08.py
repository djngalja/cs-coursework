def max_coins(matrix: list[list[int]], N: int, M: int) -> int:
    mem = matrix
    for i in range(N):
        for j in range(M):
            max_val: int = 0
            if i >= 1:
                max_val = mem[i - 1][j]
            if j >= 1:
                max_val = max(max_val, mem[i][j - 1])
            mem[i][j] += max_val
    return mem[N - 1][M - 1]

def main() -> None:
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(max_coins(matrix, N, M))

if __name__ == "__main__":
    main()