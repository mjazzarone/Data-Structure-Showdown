"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen = set()
    for id in product_ids:
        if id in seen:
            return True
        seen.add(id)
    return False

result = has_duplicates([10, 20, 30, 20, 40])
print(result)
result = has_duplicates([1, 2, 3, 4, 5])
print(result)
result = has_duplicates([1, 1, 1, 1, 1])
print(result)
result = has_duplicates([2, 2])
print(result)
result = has_duplicates([])
print(result)
result = has_duplicates([80000, 0, 80000])
print(result)
'''I chose a set for this problem becuase we are checking whether a value already exists
which is easy for a set. In the program we have a function that asks for a list of values,
stores each product ID seen into a set and if the ID is already in the set, the function returns true
If not, it returns false.'''
"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class TaskQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_task(self, task):
        new_task = Node(task)
        if not self.front:
            self.front = new_task
            self.rear = new_task
        else:
            self.rear.next = new_task
            self.rear = new_task

    def remove_oldest_task(self):
        if not self.front:
            return None
        removed_task = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_task.task
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
print(task_queue.remove_oldest_task())  
print(task_queue.remove_oldest_task())  
print(task_queue.remove_oldest_task())
'''I chose a queue for this problem because in it we are looking to deal with tasks on a first come first serve basis.
The program first sets a Node class and a front and rear node. Then add_task adds a task to the queue and puts it at the back.
Then, remove_oldest_task removes the first task executed at the front of the list.'''

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.unique_values = set()

    def add(self, value):
        self.unique_values.add(value)

    def get_unique_count(self):
        return len (self.unique_values)
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
print(tracker.get_unique_count())
'''I chose a set for this problem because we are looking to only keep track of exclusive numbers in a list.
This program initializes an empty set using __init__. add adds a value to the set, and then get_unique_count counts the number of items in the set
because a set won't accept duplicate values and will only keep exclusive ones.'''