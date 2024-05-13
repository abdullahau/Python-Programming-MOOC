# Write your solution here:
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
        return self.finished

class OrderBook:
    
    def __init__(self) -> None:
        self.orders = []
    
    def add_order(self, description: str, programmer: str, workload: str) -> None:
        self.orders.append(Task(description, programmer, workload))
     
    def all_orders(self) -> list:
        return list(self.orders)
    
    def programmers(self) -> list:
        return list(set([task.programmer for task in self.orders]))
    
    def mark_finished(self, id: int) -> None:
        for task in self.orders:
            if task.id == id:
                task.mark_finished()
                break
        else:
            raise ValueError("There is no task in the order book with the given id")

    def finished_orders(self) -> list:
        return [task for task in self.orders if task.finished]
    
    def unfinished_orders(self) -> list:
        return [task for task in self.orders if not task.finished]
    
    def status_of_programmer(self, programmer: str) -> tuple:
        finished = [task for task in self.finished_orders() if task.programmer == programmer]
        unfinished = [task for task in self.unfinished_orders() if task.programmer == programmer]
        if len(finished) == 0 and len(unfinished) == 0:
            raise ValueError("No programmer in the order book with the given name")
        return (len(finished), len(unfinished), sum(task.workload for task in finished), sum(task.workload for task in unfinished))
        
