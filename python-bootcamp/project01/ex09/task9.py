def main() -> None:
    n, dot = map(float, input().split())
    n = int(n)
    res = float()
    for _ in range(n + 1):
        num = float(input())
        res += n * num * (dot ** (n - 1))
        n -= 1
    print("{:.3f}".format(res))
    
if __name__ == "__main__":
    main()