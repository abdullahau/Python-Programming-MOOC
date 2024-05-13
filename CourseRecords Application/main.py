class Course:
    def __init__(self, name: str, grade: int, credit: int) -> None:
        self.__name = name
        self.__grade = grade
        self.__credit = credit
    
    def name(self) -> str:
        return self.__name
    
    def grade(self) -> int:
        return self.__grade
    
    def credit(self) -> int:
        return self.__credit

class CourseRecords:
    def __init__(self) -> None:
        self.__courserecord = {}
    
    def add_course(self, name: str, grade: int, credit: int):
        if name not in self.__courserecord:
            self.__courserecord[name] = Course(name, grade, credit)
        elif grade > self.__courserecord[name].grade():
            self.__courserecord[name] = Course(name, grade, credit)
    
    def course_data(self, name: str):
        if name in self.__courserecord:
            print(f"{name} ({self.__courserecord[name].credit()} cr) grade {self.__courserecord[name].grade()}")
        else:
            print("no entry for this course")
            
    def statistics(self):
        total_completed = len(self.__courserecord)
        total_credit = 0
        sum_grade = 0
        grade_list = []
        for entry in self.__courserecord.values():
            total_credit += entry.credit()
            sum_grade += entry.grade()
            grade_list.append(entry.grade())
        mean = sum_grade / total_completed
        print(f"{total_completed} completed courses, a total of {total_credit} credits")
        print(f"mean {mean:0.1f}")
        print("grade distribution")
        line = ""
        for i in range(5, 0, -1):
            x = "x" * grade_list.count(i)
            line += f"{i}: {x}\n"
        print(line[:-1])

class CourseApplication:
    def __init__(self):
        self.__courseapp = CourseRecords()
        
    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
    
    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credit: "))
        self.__courseapp.add_course(course, grade, credit)
    
    def get_course_data(self):
        course = input("course: ")
        self.__courseapp.course_data(course)
    
    def get_statistics(self):
        self.__courseapp.statistics()
        
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.get_statistics()
            else:
                self.help()    


application = CourseApplication()
application.execute()