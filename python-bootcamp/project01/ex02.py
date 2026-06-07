def inner_product(inp1: tuple[float], inp2: tuple[float]) -> float:
    res: float = 0
    for a, b in zip(inp1, inp2):
        res += a * b
    return res

def main() -> None:
    inp1 = tuple(map(float, input().split()))
    inp2 = tuple(map(float, input().split()))
    print(inner_product(inp1, inp2))

if __name__ == "__main__":
    main()