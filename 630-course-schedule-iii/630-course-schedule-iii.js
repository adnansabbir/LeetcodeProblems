/**
 * @param {number[][]} courses
 * @return {number}
 */

class MaxHeap{
    constructor(){
        this.items = []
    }
    
    push(item){
        let contains = false
        for(let i = 0; i < this.items.length; i++){
            if(this.items[i] < item){
                this.items.splice(i, 0, item)
                contains = true
                break
            }
        }
        
        if(!contains) this.items.push(item)
    }
    
    pop(){
        if(this.items.length){
            return this.items.shift()
        }   
    }
    
    peak(){
        if(this.size()) return this.items[0]
    }
    
    size(){
        return this.items.length
    }
    
    get(){
        return this.items
    }
}

var scheduleCourse = function(courses) {
    const taken = new MaxHeap()
    courses.sort((a, b)=> {
        if(a[1] === b[1]){
            return a[0] - b[0]
        }
        return a[1] - b[1]
    })
    
    let time = 0
    for(let course of courses){
        const [duration, lastday] = course
        if(time + duration <= lastday){
            taken.push(duration)
            time += duration
        }else if(taken.size() && duration < taken.peak() && (time - taken.peak() + duration < lastday)){
            time -= taken.pop()
            taken.push(duration)
            time += duration
        }
    }
    
    return taken.size()
};