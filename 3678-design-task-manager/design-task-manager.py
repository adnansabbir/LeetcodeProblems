from sortedcontainers import SortedList

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = SortedList([tuple(t) for t in tasks], key=lambda x: (x[2], x[1], x[0]))
        self.task_data = {
            t[1]: t for t in tasks
        }
        # print("Init\n", self.tasks)
            

    def add(self, userId: int, taskId: int, priority: int) -> None:
        # print("\nAdd",userId, taskId, priority)        
        self.tasks.add((userId, taskId, priority))
        self.task_data[taskId] = (userId, taskId, priority)
        # print("\n", self.tasks)

    def edit(self, taskId: int, newPriority: int) -> None:
        # print("\nEdit",taskId, newPriority)    
        userId, _, oldPriority = self.task_data[taskId]
        self.tasks.discard((userId, taskId, oldPriority))
        self.add(userId, taskId, newPriority)
        # print("\n", self.tasks)


    def rmv(self, taskId: int) -> None:
        # print("\nRem",taskId)    
        userId, _, oldPriority = self.task_data[taskId]
        self.tasks.discard((userId, taskId, oldPriority))
        del self.task_data[taskId]
        # print("\n", self.tasks)
        

    def execTop(self) -> int:
        if not len(self.tasks):
            return -1
        # print("Exec\n", self.tasks)
        return self.tasks.pop()[0]
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()