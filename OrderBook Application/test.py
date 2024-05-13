import sys
from io import StringIO

class Task:
    task_counter = 1
    
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = Task.task_counter
        Task.task_counter += 1
        
    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"
    
    def is_finished(self):
        return self.finished
    
    def mark_finished(self):
        self.finished = True

class OrderBook:
    
    def __init__(self) -> None:
        self.__orders = []
    
    def add_order(self, description: str, programmer: str, workload: str) -> None:
        self.__orders.append(Task(description, programmer, workload))
     
    def all_orders(self) -> list:
        return self.__orders
    
    def programmers(self) -> list:
        return list(set([task.programmer for task in self.__orders]))
    
    def mark_finished(self, id: int) -> None:
        for task in self.__orders:
            if task.id == id:
                task.mark_finished()
                break
        else:
            raise ValueError("There is no task in the order book with the given id")

    def finished_orders(self) -> list:
        return [task for task in self.__orders if task.finished]
    
    def unfinished_orders(self) -> list:
        return [task for task in self.__orders if not task.finished]
    
    def status_of_programmer(self, programmer: str) -> tuple:
        finished = [task for task in self.finished_orders() if task.programmer == programmer]
        unfinished = [task for task in self.unfinished_orders() if task.programmer == programmer]
        if len(finished) == 0 and len(unfinished) == 0:
            raise ValueError("No programmer in the order book with the given name")
        return (len(finished), len(unfinished), sum(task.workload for task in finished), sum(task.workload for task in unfinished))

class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()
    
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")  
        print("6 status of programmer")
        
    def add_order(self):
        description = input("description: ")
        programmer, workload = input("programmer and workload estimate: ").split()
        self.__orderbook.add_order(description, programmer, int(workload))
        print("added!")
        
    def finished_orders(self):
        if len(self.__orderbook.finished_orders()) > 0:
            for task in self.__orderbook.finished_orders():
                print(task)
        else:
            print("no finsihed tasks")
    
    def unfinished_orders(self):
        if len(self.__orderbook.unfinished_orders()) > 0:
            for task in self.__orderbook.unfinished_orders():
                print(task)
        else:
            print("no unfinsihed tasks")
            
    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)
    
    def mark_finished(self):
        id = int(input("id: "))
        self.__orderbook.mark_finished(id)
        print("marked as finished")
    
    def programmer_status(self):
        programmer = input("programmer: ")
        finished, unfinished, finished_workload, unfinished_workload = self.__orderbook.status_of_programmer(programmer)
        print(f"tasks: finished {finished} not finished {unfinished}, hours: done {finished_workload} scheduled {unfinished_workload}")
    
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.finished_orders()
            elif command == "3":
                self.unfinished_orders()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.programmer_status()
            else:
                continue

application = OrderBookApplication()

with open("input.txt") as f:
    for i in f:
        sys.stdin = StringIO(i.strip())
        application.execute()