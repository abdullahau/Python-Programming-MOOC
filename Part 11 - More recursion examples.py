# More recursion example

# The real advantages of recursion become evident when we come across problems where iterative solutions are difficult to write. 

# Let's take a look at _binary trees_, for instance. 
# A binary tree is a branched structure where we have nodes, and at each node the structure branches, at most, into two child branches with nodes of their own. 

# Binary trees should at least theoretically be easy to handle recursively: if we want to perform some operation on every node in the tree, our algorithm simply needs to
    # 1. Process the current node
    # 2. Call itself on the child node on the left 
    # 3. Call itself on the child node on the right

# Both the left and right "subtrees" are fully fledged binary trees themselves, and the only node left outside the recursive calls is the parent node, which is processed in step 1, before calling the function recursively. 
# So, we can be sure that when the execution of the function finishes, each node has been visited exactly once. 

# An iterative version of a binary tree traversal would be much more complicated, as we would have to somehow keep track of all the nodes we have already visited. 
# The same principles are true for all computational tree structures, not just binary ones.

# A binary tree is easily modelled in Python code as well. 
# We only need to write a class definition for a single node. 
# It has a value attribute and attributes for the left and right child nodes:

class Node:
    """ The class represents a single node in a binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        
# Now let's assume we want to model the following tree: Images\11_4_3.png
tree = Node(2)

tree.left_child = Node(3)
tree.left_child.left_child = Node(5)
tree.left_child.right_child = Node(8)

tree.right_child = Node(4)
tree.right_child.right_child = Node(11)

# Recursive binary tree algorithms

# First, let's take a look at an algorithm which prints out all the nodes in a binary tree one by one. 
# In these following examples we will be working with the binary tree defined above.

# The argument to the printing function is the root node of the binary tree. 
# This is the node at the very top. All other nodes are _children_ to this node:

def print_nodes(root: Node):
    print(root.value)

    if root.left_child is not None:
        print_nodes(root.left_child)

    if root.right_child is not None:
        print_nodes(root.right_child)

 # The function prints the value of the node passed as an argument, and then calls itself on the left and right child nodes, assuming the nodes are defined. 
 # This is a very simple algorithm, but it efficiently and reliably traverses all nodes in the tree, no matter the size of the tree. 
 # Crucially, no node is visited twice. Each value is printed only once.
 
 # If we pass the root node `tree` of the binary tree illustrated above as an argument to the function, it prints out
 
 
class Node:
    """ The class represents a single node in a binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
 
tree = Node(2)

tree.left_child = Node(3)
tree.left_child.left_child = Node(5)
tree.left_child.right_child = Node(8)

tree.right_child = Node(4)
tree.right_child.right_child = Node(11)

def print_nodes(root: Node):
    print(root.value)

    if root.left_child is not None:
        print_nodes(root.left_child)

    if root.right_child is not None:
        print_nodes(root.right_child)

print_nodes(tree)

# As you can see from the order of the nodes in the printout, the algorithm first moves down the "left leg" of the tree down to the very bottom, and from there traverses the other nodes in order.

# Similarly, we can write an algorithm for calculating the sum of all the values stored in the nodes of the tree:
def sum_of_nodes(root: Node):
    node_sum = root.value

    if root.left_child is not None:
        node_sum += sum_of_nodes(root.left_child)

    if root.right_child is not None:
        node_sum += sum_of_nodes(root.right_child)

    return node_sum

sum_of_nodes(tree)

# The variable `node_sum` is initialised to equal the value of the current node. 
# The value in the variable is then augmented by recursive calls to the node sums of the left and right child trees (first making sure they exist, of course). 
# This result is then returned.

# Greatest node

# Please write a function named `greatest_node(root: Node)` which takes the root node of a binary tree as its argument.

# The function should return the node with the greatest value within the tree. The tree should be traversed recursively.

# Hint: the function `sum_of_nodes` in the example above may come in handy.

class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        

def greatest_node(root: Node):
    node_large = root.value
    
    if root.left_child is not None:
        if greatest_node(root.left_child) > node_large:
            node_large = greatest_node(root.left_child)
    
    if root.right_child is not None:
        if greatest_node(root.right_child) > node_large:
            node_large = greatest_node(root.right_child)
    
    return node_large

tree = Node(2)

tree.left_child = Node(3)
tree.left_child.left_child = Node(5)
tree.left_child.right_child = Node(8)

tree.right_child = Node(4)
tree.right_child.right_child = Node(11)

print(greatest_node(tree))

# Greatest Node - Approach 2
def greatest_node(root: Node):
    value = root.value
 
    if root.left_child:
        left_value = greatest_node(root.left_child)
    else:
        left_value = value
 
    if root.right_child:
        right_value = greatest_node(root.right_child)
    else:
        right_value = value
 
    return max(value, left_value, right_value)


# A sorted binary tree

# A binary tree is especially useful when the nodes are sorted in a certain way. 
# This makes finding nodes in the tree fast and efficient.

# Let's take a look a tree which is sorted as follows: the left child of each node is smaller than the node itself, and the right child is correspondingly greater.

tree = Node(7)

tree.left_child = Node(11)
tree.left_child.left_child = Node(14)
tree.left_child.left_child.left_child = Node(16)
tree.left_child.left_child.right_child = Node(9)

tree.right_child = Node(3)
tree.right_child.left_child = Node(5)
tree.right_child.left_child.right_child = Node(4)
tree.right_child.right_child = Node(2)


# Now we can write a recursive algorithm for searching for nodes. 
# The idea is very similar to the binary search from the previous section: if the current node is the node we are looking for, return `True`. 
# Else, continue recursively with either the left or the right child tree. If the node is not defined, return `False`.

def find_node(root: Node, value):
    if root is None:
        return False

    if value == root.value:
        return True

    if value > root.value:
        return find_node(root.right_child, value)

    return find_node(root.left_child, value)

# Bosses and subordinates - Approach 1

# The class `Employee` models an employee of a company:

class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

# Please write a function named `count_subordinates(employee: Employee)` which recursively counts the number of subordinates each employee has.

def count_subordinates(employee: Employee):
    total_subordinates = 0
    
    if len(employee.subordinates) > 0:
        total_subordinates += len(employee.subordinates)
        
        for i in employee.subordinates:  
            total_subordinates += count_subordinates(i)

    return total_subordinates
    

if __name__ == "__main__":
    t1 = Employee("Sally")
    t2 = Employee("Eric")
    t3 = Employee("Matthew")
    t4 = Employee("Emily")
    t5 = Employee("Adele")
    t6 = Employee("Claire")
    t1.add_subordinate(t4)
    t1.add_subordinate(t6)
    t4.add_subordinate(t2)
    t4.add_subordinate(t3)
    t4.add_subordinate(t5)
    print(count_subordinates(t1))
    print(count_subordinates(t4))
    print(count_subordinates(t5))
    

# Bosses and subordinates - Approach 2

def count_subordinates(employee: Employee):
    if employee is None:
        return 0
    no_of_subordinates = 0
    for subordinate in employee.subordinates:
        no_of_subordinates += count_subordinates(subordinate)+1 # +1 captures the immediate child object in the branch
    return no_of_subordinates


# Revisiting the times before recursion

# Let's finish off this part of the material with a slightly larger exercise concentrating on object oriented programming principles. 
# We do not recommend using recursion in this series of tasks, but list comprehension techniques will come in useful.

# OrderBook

# In this exercise you will write two different classes, which will in turn form the backbone of the programming exercise which follows this one, where you will write an interactive application.

# Part 1: Task

# Please write a class named `Task` which models a single task in a software company's list of tasks. Tasks have:
    # - a description
    # - an estimate of the hours required for completing the task
    # - the name of the programmer assigned to the task
    # - a field for keeping track of whether the task is finished
    # - a unique identifier

# Some clarifications:
    # - the state of the task (finished or not yet finished) can be checked with the function `is_finished(self)` which returns a Boolean value
    # - a task is not finished when it is created
    # - a task is marked as finished by calling the method `mark_finished(self)`
    # - the id of a task is a running number which starts with 1. The id of the first task is 1, the id of the second is 2, and so forth.

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

t1 = Task("program hello world", "Eric", 3)
print(t1.id, t1.description, t1.programmer, t1.workload)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())
t2 = Task("program webstore", "Adele", 10)
t3 = Task("program mobile app for workload accounting", "Eric", 25)
print(t2)
print(t3)

# **Hint**: `id` can be implemented as a [class variable](/part-9/5-class-attributes#class-variables).

# Part 2: OrderBook

# Please write a class named `OrderBook` which collects all the tasks ordered from the software company. 
# The tasks should be modelled with the class `Task` you just wrote.

# At this stage your `OrderBook` should provide three methods:
    # - `add_order(self, description, programmer, workload)` which adds a new order to the OrderBook. An OrderBook stores the orders internally as `Task` objects. 
        # NB: the method should take exactly the arguments mentioned, or else the automated tests will not work correctly.
    # - `all_orders(self)` returns a list of all the tasks stored in the OrderBook
    # - `programmers(self)` returns a list of the names of all the programmers with tasks stored in the OrderBook. The list should contain each programmer only once

class OrderBook:
    
    def __init__(self) -> None:
        self.orders = []
    
    def add_order(self, description: str, programmer: str, workload: str):
        self.orders.append(Task(description, programmer, workload))
     
    def all_orders(self) -> list:
        return list(self.orders)
    
    def programmers(self) -> list:
        return list(set([task.programmer for task in self.orders]))
           

orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

for order in orders.all_orders():
    print(order)

print()

for programmer in orders.programmers():
    print(programmer)


# **Hint:** an easy method for removing duplicates is handling the list initially as a [set](https://docs.python.org/3.8/library/stdtypes.html#set). 
# A set is a collection of items where each unique item appears only once. 
# A `set` can be then converted back into a list, and we can then be sure each item is now unique:
my_list = [1,1,3,6,4,1,3]
my_list2 = list(set(my_list))
print(my_list)
print(my_list2)
    
# Part 3: Some more features for OrderBook

# Please write three more methods in your `OrderBook` class.

# The method `mark_finished(self, id: int)` takes the id of the task as its argument and marks the relevant task as finished.

# If there is no task with the given id, the method should raise a `ValueError` exception. 
# If you need a refresher on raising exceptions, please have a look at [part 6](/part-6/3-errors#raising-exceptions).

# The methods `finished_orders(self)` and `unfinished_orders(self)` work as expected: both return a list containing the relevant tasks from the OrderBook.

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

    def finished_orders(self):
        return [task for task in self.orders if task.finished]
    
    def unfinished_orders(self):
        return [task for task in self.orders if not task.finished]


orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

orders.mark_finished(1)
orders.mark_finished(5)

for order in orders.all_orders():
    print(order)
    

# Part 4: Finishing touches to OrderBook

# Please write one last method in your `OrderBook` class: `status_of_programmer(self, programmer: str)` which returns a _tuple_. 
# The tuple should contain the number of finished and unfinished tasks the programmer has assigned to them, along with the estimated hours in both categories.

# The first item in the tuple is the number of _finished_ tasks, while the second item is the number of _unfinished_ tasks. 
# The third and fourth items are the sums of workload estimates for the finished and unfinished tasks, respectively.

# If there is no programmer with the given name, the method should raise a `ValueError` exception.

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
        self.orders = []
    
    def add_order(self, description: str, programmer: str, workload: str) -> None:
        self.orders.append(Task(description, programmer, workload))
     
    def all_orders(self) -> list:
        return self.orders
    
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

orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Adele", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.add_order("program the next facebook", "Eric", 1000)

orders.mark_finished(1)
orders.mark_finished(2)

status = orders.status_of_programmer("Adele")
print(status)

# OrderBook Approach 2
class Task:
    id = 0
    @classmethod 
    def new_id(cls):
        Task.id += 1
        return Task.id
 
    def __init__(self, description, programmer, workload):
        self.programmer = programmer
        self.description = description
        self.workload = workload
        self.id = Task.new_id()
        self.finished = False
    
    def is_finished(self):
        return self.finished 
 
    def mark_finished(self):
        self.finished = True
 
    def __str__(self):
        status = "NOT FINISHED" if not self.finished else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"
 
class OrderBook:
    def __init__(self):
        self.__tasks = []
 
    def add_order(self, description, programmer, workload):
        self.__tasks.append(Task(description, programmer, workload))
 
    def all_orders(self):
        return self.__tasks
 
    def programmers(self):
        return list(set([t.programmer for t in self.__tasks]))
 
    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        
        # not incorrect
        raise ValueError("wrong id")
    
    def unfinished_orders(self):
        return [t for t in self.__tasks if not t.is_finished()]
 
    def finished_orders(self):
        return [t for t in self.__tasks if t.is_finished()]
 
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer does not exists")
        
        finished_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished() ]
        not_finished_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished() ]
 
        finished_hours = sum(t.workload for t in finished_tasks)
        not_finished_hours = sum(t.workload for t in not_finished_tasks)
 
        return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)

# Order book application - Approach 1

# In this exercise you will create an interactive application for administering the tasks ordered from a software company. 
# The implementation is completely up to you, but you may use the building blocks from the previous exercise in your application. 
# The examples in the [last section of part 10](/part-10/4-application-development) can also prove useful.

# Part 1: Without error handling

# The application should work exactly as follows:

'''
commands:
0 exit
1 add order
2 list finished tasks
3 list unfinished tasks
4 mark task as finished
5 programmers
6 status of programmer

command: 1
description: program the next facebook
programmer and workload estimate: jonah 1000
added!

command: 1
description: program mobile app for workload accounting
programmer and workload estimate: eric 25
added!

command: 1
description: program an app for music theory revision
programmer and workload estimate: nina 12
added!

command: 1
description: program the next twitter
programmer and workload estimate: jonah 55
added!

command: 2
no finished tasks

command: 3
1: program the next facebook (1000 hours), programmer jonah NOT FINISHED
2: program mobile app for workload accounting (25 hours), programmer eric NOT FINISHED
3: program an app for music theory revision (12 hours), programmer nina NOT FINISHED
4: program the next twitter (55 hours), programmer jonah NOT FINISHED

command: 4
id: 2
marked as finished

command: 4
id: 4
marked as finished

command: 2
2: program mobile app for workload accounting (25 hours), programmer eric FINISHED
4: program the next twitter (55 hours), programmer jonah FINISHED

command: 3
1: program the next facebook (1000 hours), programmer jonah NOT FINISHED
3: program an app for music theory revision (12 hours), programmer nina NOT FINISHED

command: 5
jonah
eric
nina

command: 6
programmer: jonah
tasks: finished 2 not finished 1, hours: done 55 scheduled 1000
'''

# Part 2: Handling errors in user input

# To gain the second exercise point for this exercise your application is expected to recover from erroneus user input. 
# Any input which does not follow the specified format should produce an error message _erroneous input_, and result in yet another repeat of the loop asking for a new command:

'''
command: **1**
description: **program mobile app for workload accounting**
programmer and workload estimate: **eric xxx**
erroneous input

command: **1**
description: **program mobile app for workload accounting**
programmer and workload estimate: **eric**
erroneous input

command: **4**
id: **1000000**
erroneous input

command: **4**
id: **XXXX**
erroneous input

command: **6**
programmer: **unknownprogrammer**
erroneous input
'''

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
        programmer_workload = input("programmer and workload estimate: ").split()
        if len(programmer_workload) != 2:
            print("erroneous input")
            return
        elif not programmer_workload[1].isdigit():
            print("erroneous input")
            return
        self.__orderbook.add_order(description, programmer_workload[0], int(programmer_workload[1]))
        print("added!")
        
    def finished_orders(self):
        if len(self.__orderbook.finished_orders()) > 0:
            for task in self.__orderbook.finished_orders():
                print(task)
        else:
            print("no finished tasks")
    
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
        id = input("id: ")
        if not id.isdigit():
            print("erroneous input")
            return
        elif int(id) not in [order.id for order in self.__orderbook.all_orders()]:
            print("erroneous input")
            return
        self.__orderbook.mark_finished(int(id))
        print("marked as finished")
    
    def programmer_status(self):
        programmer = input("programmer: ")
        if programmer not in self.__orderbook.programmers():
            print("erroneous input")
            return
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
application.execute()


# Order book application - Approach 2

class Task:
    id = 0
    @classmethod 
    def new_id(cls):
        Task.id += 1
        return Task.id
 
    def __init__(self, description, programmer, workload):
        self.programmer = programmer
        self.description = description
        self.workload = workload
        self.id = Task.new_id()
        self.finished = False
    
    def is_finished(self):
        return self.finished 
 
    def mark_finished(self):
        self.finished = True
 
    def __str__(self):
        status = "NOT FINISHED" if not self.finished else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"
 
class OrderBook:
    def __init__(self):
        self.__tasks = []
 
    def add_order(self, description, programmer, workload):
        self.__tasks.append(Task(description, programmer, workload))
 
    def all_orders(self):
        return self.__tasks
 
    def programmers(self):
        return list(set([t.programmer for t in self.__tasks]))
 
    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        
        # not incorrect
        raise ValueError("wrong id")
    
    def unfinished_orders(self):
        return [t for t in self.__tasks if not t.is_finished()]
 
    def finished_orders(self):
        return [t for t in self.__tasks if t.is_finished()]
 
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer does not exists")
        
        finished_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished() ]
        not_finished_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished() ]
 
        finished_hours = sum(t.workload for t in finished_tasks)
        not_finished_hours = sum(t.workload for t in not_finished_tasks)
 
        return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)
 
class Application:
    def __init__(self):
        self.orders = OrderBook()
 
    def instructions(self):
        # Defining multiline string is possible with triple apostrophes
        instructions_str = """
commands:
0 exit
1 add order
2 list finished tasks
3 list unfinished tasks
4 mark task as finished
5 programmers
6 status of programmer"""
        print(instructions_str)
 
    def add(self):
        description = input("description: ")
        programmer_and_estimate = input("programmer and workload estimate: ")
        try:
            programmer = programmer_and_estimate.split(' ')[0]
            workload = int(programmer_and_estimate.split(' ')[1])
            self.orders.add_order(description, programmer, workload)
            print("added!")
        except:
            print("erroneous input")
 
    def unfinished(self):
        for task in self.orders.unfinished_orders():
            print(task)
 
    def finished(self):
        finished_orders = self.orders.finished_orders()
        if len(finished_orders)==0:
            print("no finished tasks")
            return
 
        for task in finished_orders:
            print(task)
 
    def programmers(self):
        for programmer in self.orders.programmers():
            print(programmer)
 
    def mark_finished(self):
        try:
            order_id = int(input("id: "))
            self.orders.mark_finished(order_id)
            print("marked as finished")
        except:
            print("erroneous input")
 
    def programmers_status(self):
        programmer = input("programmer: ")
        if not programmer in self.orders.programmers():
            print("erroneous input")
            return
 
        status = self.orders.status_of_programmer(programmer)
        print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
 
    def run(self):
        self.instructions()
        while True:
            command = input("command: ")
            if command == "0":
                return
            elif command == "1":
                self.add()
            elif command == "2":
                self.finished()
            elif command == "3":
                self.unfinished()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.programmers_status()
            print()
 
Application().run()