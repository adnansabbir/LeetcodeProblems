class Event:
    def __init__(self, start: int, end: int, left: 'Event' = None, right: 'Event' = None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right
    
    def intersects(self, event: 'Event')-> bool:
        return not ((event.start <= self.start and event.end <= self.start) or (event.start >= self.end and event.end >= self.end))
    
    def __lt__(self, event: 'Event')-> bool:
        return self.end <= event.start
    
    def __gt__(self, event: 'Event')-> bool:
        return self.start >= event.end
    
    def __str__(self)-> str:
        return f'[{self.start, self.end} ->\tLeft : {self.left} \tRight : {self.right})'

class MyCalendar:

    def __init__(self):
        self.events = None
    
    def book(self, start: int, end: int) -> bool:
        if not self.events:
            self.events = Event(start, end)
            return True
        
        tempParent = self.events
        newEvent = Event(start, end)
        
        while not tempParent.intersects(newEvent):
            if newEvent < tempParent:
                if not tempParent.left:
                    tempParent.left = newEvent
                    return True
                else:
                    tempParent = tempParent.left
            elif newEvent > tempParent:
                if not tempParent.right:
                    tempParent.right = newEvent
                    return True
                else:
                    tempParent = tempParent.right
        
        return False
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)