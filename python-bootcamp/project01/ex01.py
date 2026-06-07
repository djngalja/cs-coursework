def get_data(N: int, my_dict: dict) -> None:
    for _ in range(N):
        year, price, time = map(int, input().split())
        if (year > 0 and price > 0 and time > 0):
            if year not in my_dict:
                my_dict[year] = {}
            if (time not in my_dict[year] or my_dict[year][time] > price):
                my_dict[year][time] = price 
        else:
            raise ValueError 

def get_min_ttl_price(ttl_time: int, my_dict: dict) -> int:
    res = int()
    for year in my_dict:
        if len(my_dict[year]) < 2:
            continue
        for time in my_dict[year]:
            if ttl_time - time in my_dict[year]:
                temp_res: int = my_dict[year][time] + my_dict[year][ttl_time - time]
                if (res == 0 or (res !=0 and temp_res < res)):
                    res = temp_res
    return res

def main() -> None:
    try:
        N, ttl_time = map(int, input().split())
        if (N > 0 and ttl_time > 0):
            my_dict = dict()
            get_data(N, my_dict)
            print(get_min_ttl_price(ttl_time, my_dict))
        else:
            raise ValueError
    except ValueError:
        print("Error: invalid input")
    
if __name__ == "__main__":
    main()