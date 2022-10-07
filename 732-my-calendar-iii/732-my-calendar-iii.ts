class MyCalendarThree {
    public eventDates: Record<number, number>
    constructor() {
        this.eventDates = {}
    }

    book(start: number, end: number): number {
        this.eventDates[start] = (this.eventDates[start] || 0) + 1
        this.eventDates[end] = (this.eventDates[end] || 0) - 1
        let maxK = 0, runningEvent = 0
        
        Object.values(this.eventDates).forEach(event=> {
            runningEvent += event
            maxK = Math.max(runningEvent, maxK)
        })
        
        return maxK
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * var obj = new MyCalendarThree()
 * var param_1 = obj.book(start,end)
 */