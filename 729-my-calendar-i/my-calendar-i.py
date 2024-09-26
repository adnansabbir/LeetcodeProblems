from bisect import bisect

class MyCalendar:
    def __init__(self):
        self.bookings = []
        

    def book(self, start: int, end: int) -> bool:
        if not len(self.bookings):
            self.bookings.append((start, end))
            return True
        else:
            pos = bisect(self.bookings, (start, end))
            
            # check if collides with prev
            if pos != 0:
                if start < self.bookings[pos-1][1]:
                    return False
            # check if it collides with next
            if pos != len(self.bookings):
                if end > self.bookings[pos][0]:
                    return False
            self.bookings.insert(pos, (start, end))
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)