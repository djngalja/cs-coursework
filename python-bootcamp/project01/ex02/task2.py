def is_palindrome(num: int) -> bool:
    if num < 0:
        return False
    num_copy: int = num
    num_rev: int = 0
    while num > 0:
        digit: int = num % 10
        num_rev = num_rev * 10 + digit
        num //= 10
    return num_copy == num_rev

def main() -> None:
    inp: int = int(input())
    print(is_palindrome(inp))

if __name__ == "__main__":
    main()