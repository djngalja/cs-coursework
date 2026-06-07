def main() -> None:
    N: int = int(input())
    my_set = set()
    for _ in range(N):
        my_set.add(int(input()))
    print(len(my_set))
    
if __name__ == "__main__":
    main()