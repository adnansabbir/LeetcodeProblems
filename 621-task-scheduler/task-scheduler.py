class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_frequency = max(task_counts.values())
        max_frequency_tasks = sum(1 for task, count in task_counts.items() if count == max_frequency)
        
        # Calculate the minimum time directly
        part_count = max_frequency - 1
        part_length = n - (max_frequency_tasks - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_frequency * max_frequency_tasks
        idles = max(0, empty_slots - available_tasks)

        return len(tasks) + idles

        