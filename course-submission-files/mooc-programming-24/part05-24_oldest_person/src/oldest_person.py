# Write your solution here
def oldest_person(people: list):
    ref = 0
    index = 0
    for person in people:
        if person[1] < ref or ref == 0:
            ref = person[1]
            index = people.index(person)
    return people[index][0]

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))