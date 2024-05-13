# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", "a") as database:
        line = ""
        for data in person:
            line += f"{data};"
        line = line[:-1]
        database.write("\n" + line)
        
if __name__ == "__main__": 
    store_personal_data(("Paul Paulson", 37, 175.5))