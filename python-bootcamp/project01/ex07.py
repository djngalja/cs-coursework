import json
import os

def merge_two_sorted_lists(data: json) -> dict[str, list]:
    listn = [list_name for list_name in data.keys()]
    id0: int = 0
    id1: int = 0
    lim0: int = len(data[listn[0]])
    lim1: int = len(data[listn[1]])
    new_list = []
    while(id0 < lim0 and id1 < lim1):
        if data[listn[0]][id0]["year"] < data[listn[1]][id1]["year"]:
            new_list.append(data[listn[0]][id0])
            id0 += 1
        else:
           new_list.append(data[listn[1]][id1]) 
           id1 += 1
    while id0 < lim0:
        new_list.append(data[listn[0]][id0])
        id0 += 1
    while id1 < lim1:
        new_list.append(data[listn[1]][id1]) 
        id1 += 1
    return {"list0": new_list}

def main() -> None:
    try:
        file_sz: int = os.path.getsize("input.txt")
        if file_sz != 0:
            with open("input.txt", "r") as file:
                data: json = json.load(file)
            output_dict: dict[str, list] = merge_two_sorted_lists(data)
            print(json.dumps(output_dict, indent=2))
        else:
            print("Empty file")
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("Invalid input")
    
if __name__ == "__main__":
    main()