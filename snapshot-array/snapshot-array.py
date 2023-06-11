class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [{0: {'val': 0}} for i in range(length)]
        self.version = 0
        

    def set(self, index: int, val: int) -> None:
        # print(self.arr)
        data = self.arr[index]
        v = self.version
        # print(v, data)
        if v not in data:
            data[v] = {'val': 0}

        data[v]['val'] = val
        # print(self.arr)
        # print('\n')

    def snap(self) -> int:
        self.version += 1
        return self.version - 1

    def get(self, index: int, snap_id: int) -> int:
        # print('Getting ', index, snap_id)
        data = self.arr[index]
        snap_id = self.get_nearest_snap_id(index, snap_id)
        # print('Data before', snap_id)
        # if snap_id not in data:
            # lastVData = data[0]['val']
            # for i in range(snap_id + 1):
            #     if i in data:
            #         lastVData = data[i]
            #     else:
            #         data[i] = lastVData
        
        # print('Data after', snap_id)
        return data[snap_id]['val']
        return 0
    
    def get_nearest_snap_id(self, index: int, snap_id: int)-> int:
        data = self.arr[index]
        if snap_id in data:
            return snap_id

        versions = list(data.keys())
        start, end = 0, len(versions) - 1

        while start <= end:
            mid = (start + end) // 2
            if versions[mid] <= snap_id and (mid == end or versions[mid + 1] > snap_id):
                return versions[mid]
            elif versions[mid] > snap_id:
                end = mid - 1
            else:
                start = mid + 1
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)