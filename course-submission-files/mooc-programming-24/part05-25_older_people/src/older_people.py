# Write your solution here
def older_people(people: list, year: int):
    shortlist = []
    for person in people:
        if person[1] < year:
            shortlist.append(person[0])
    return shortlist