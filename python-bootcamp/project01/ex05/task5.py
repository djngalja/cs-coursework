def validate(inp: str) -> bool:
    res: bool = True
    if not(inp[0] == '-' or inp[0] == '+' 
           or (inp[0] >= '0' and inp[0] <= '9')):
        res = False 
    cnt_dot: int  = 0
    for i in range(1, len(inp)):
        if inp[i] == '.':
            cnt_dot += 1
        elif (inp[i] < '0' or inp[i] > '9'):
            res = False
    if cnt_dot > 1:
        res = False
    return res
        
def get_num(inp: str) -> float:
    positive: bool = False if inp[0] == '-' else True
    pos: int = 1 if (inp[0] == '-' or inp[0] == '+') else 0
    num: float = ord(inp[pos]) - ord('0')
    pos += 1
    while (pos < len(inp) and inp[pos] != '.'):
        num *= 10
        num += ord(inp[pos]) - ord('0')
        pos += 1
    pos += 1
    cnt_fraction: int = 0
    while pos < len(inp):
        cnt_fraction += 1
        temp: float = ord(inp[pos]) - ord('0')
        num += temp / (10 ** cnt_fraction)
        pos += 1
    if not positive:
        num *= -1
    return num

def main() -> None:
    inp = input()
    if validate(inp):
        print("{:.3f}".format(get_num(inp) * 2))
    else:
        print("Error: invalid input")

if __name__ == "__main__":
    main()