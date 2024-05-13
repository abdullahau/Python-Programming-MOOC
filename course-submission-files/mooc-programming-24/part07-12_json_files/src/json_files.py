# Write your solution here
import json


def print_persons(filename: str): 
    with open(filename) as my_file:
        data = json.loads(my_file.read())
        
    for i in data:
        print(f"{i["name"]} {i["age"]} years ({", ".join(i["hobbies"])})")
        
if __name__ == "__main__":
    print_persons("file2.json")