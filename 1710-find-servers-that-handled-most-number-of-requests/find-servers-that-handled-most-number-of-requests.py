from sortedcontainers import SortedSet

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free_servers = SortedSet([i for i in range(k)])
        busy_servers = SortedSet([])
        server_task_count = {}
        max_served = 0

        def free_up_servers(t):
            while busy_servers and busy_servers[0][0] <= t:
                task_completed_server = busy_servers.pop(0)
                free_servers.add(task_completed_server[1])
                # print(f"{task_completed_server} popped at time: {t}")
                # print(f"Server State | Free: {free_servers}, Busy: {busy_servers}")

        def process_task(s, a, l):
            if not len(free_servers):
                # print("Dropped")
                return -1
            free_server_idx = free_servers.bisect_left(s)
            # print(f"Trying server: {s} and got index {free_server_idx}")
            selected_server = None
            if free_server_idx == len(free_servers):
                selected_server = free_servers.pop(0)
            else:
                selected_server = free_servers.pop(free_server_idx)

            busy_servers.add((a + l, selected_server))

            server_task_count[selected_server] = server_task_count.get(selected_server, 0) + 1
            # print(f"Server State | Selected: {selected_server} Free: {free_servers}, Busy: {busy_servers}")
            return server_task_count[selected_server]

        for i in range(len(arrival)):
            a, l = (arrival[i], load[i])
            # print(f"Processing arrival: {a} and Load: {l}")
            target_server = i % k
            # print(f"Target Server: {target_server}")
            free_up_servers(a)
            max_served = max(max_served, process_task(target_server, a, l))
            # print("\n")

        # print(server_task_count)
        # print([k for k, v in server_task_count.items() if v == max_served])
        return [k for k, v in server_task_count.items() if v == max_served]