# Write your solution here
def list_of_stars(list: list):
    for i in list:
        print("*" * i)
        
if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])