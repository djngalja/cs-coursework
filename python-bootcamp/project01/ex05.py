def pascal(num: int) -> None:
    for i in range(num):
        k: int = 1
        for j in range(0, i + 1):
            print(k, '', end='')
            k = k * (i - j) // (j + 1)
        print()

def main() -> None:
    inp = input()
    if (inp.isdigit() and int(inp) > 0):
        pascal(int(inp))
    else:
        print("Natural number was expected")

if __name__ == "__main__":
    main()