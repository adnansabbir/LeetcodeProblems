class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_frequency = max(task_counts.values())
        max_frequency_tasks = sum(1 for task, count in task_counts.items() if count == max_frequency)
        
        idle_time_in_between = 0
        if n <= max_frequency_tasks - 1:
            total_time = max_frequency * max_frequency_tasks
        else:
            idle_in_each_group = n - (max_frequency_tasks - 1)
            time_to_complete_each_group = max_frequency_tasks + idle_in_each_group
            total_time = (time_to_complete_each_group * max_frequency) - idle_in_each_group
            idle_time_in_between = (max_frequency * idle_in_each_group) - idle_in_each_group

        tasks_left = len(tasks) - (max_frequency * max_frequency_tasks)
        tasks_left_after_idle_time = max(0, tasks_left - idle_time_in_between)
        return total_time + tasks_left_after_idle_time

        