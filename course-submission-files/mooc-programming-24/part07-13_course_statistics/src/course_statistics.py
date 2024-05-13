# Write your solution here
import urllib.request
import json

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(my_request.read())

    retrieved_list = []
    for i in data:
        if i["enabled"] == True:
            retrieved_tuple = i["fullName"], i["name"], i["year"], sum(i["exercises"])
            retrieved_list.append(retrieved_tuple)

    return retrieved_list

def retrieve_course(course_name: str) -> dict:
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats"
    my_request = urllib.request.urlopen(url)
    data = json.loads(my_request.read())
    
    course_dict = {}
    students, hours, exercises = 0, 0, 0
    for week in data:
        if data[week]["students"] > students:
            students = data[week]["students"]

        hours += data[week]["hour_total"]
        
        exercises += data[week]["exercise_total"]
    
    course_dict['weeks'] = len(data) 
    course_dict['students'] = students
    course_dict["hours"] = hours
    course_dict["hours_average"] = hours // students
    course_dict["exercises"] = exercises
    course_dict["exercises_average"] = exercises //students
    return course_dict

if __name__ == "__main__":
    retrieve_all()
    retrieve_course("docker2019")