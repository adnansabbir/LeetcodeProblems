class UndergroundSystem:

    def __init__(self):
        self.checkedInCustomers = {}
        self.averageTime = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedInCustomers[id] = {'station': stationName, 'time': t}
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.checkedInCustomers[id]['station']
        startTime = self.checkedInCustomers[id]['time']

        if startStation not in self.averageTime:
            self.averageTime[startStation] = {}

        if stationName not in self.averageTime[startStation]:
             self.averageTime[startStation][stationName] = {'total': t - startTime, 'count': 1}
        else:
            self.averageTime[startStation][stationName]['total'] += t - startTime
            self.averageTime[startStation][stationName]['count'] += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime = self.averageTime[startStation][endStation]['total']
        count = self.averageTime[startStation][endStation]['count']
        return totalTime/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)