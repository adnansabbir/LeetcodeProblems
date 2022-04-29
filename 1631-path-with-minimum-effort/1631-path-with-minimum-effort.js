class PriorityQueue{
	constructor(){
		this.heap = []
	}
	
	add(diff, idx){
		this.heap.push({diff, idx})
		this.perkUp()
	}
	
	perkUp(){
		let childIdx = this.heap.length - 1
		
		while(childIdx){
			const parentIdx = parseInt((childIdx - 1) / 2)
			const p = this.heap[parentIdx]
			const c = this.heap[childIdx]
		
			if(p.diff > c.diff){
				this.heap[parentIdx] = this.heap[childIdx]
				this.heap[childIdx] = p
				childIdx = parentIdx
			}else{
				break;
			}
		}
		
	}
	
	get(){
		const last = this.heap[this.heap.length-1]
		const first = this.heap[0]
		
		this.heap[0] = last
		this.heap[this.heap.length-1] = first
		
		this.heap.pop()
		this.perkDown()
		
		return first
	}
	
	getMinChild(parentIdx){
		const maxIdx = this.heap.length - 1
		const childs = [(parentIdx * 2) + 1, (parentIdx * 2) + 2]
		if(childs[1] > maxIdx){
			childs.pop()
		}
		
		if(childs[0] > maxIdx){
			childs.pop()
		}
		
		if(!childs.length) return -1
		if(childs.length === 1 || this.heap[childs[0]].diff <= this.heap[childs[1]].diff) return childs[0]
		return childs[1]
	}
	
	perkDown(){
		let parentIdx = 0
		const maxIdx = this.heap.length - 1
		while(parentIdx < maxIdx){
			const childIdx = this.getMinChild(parentIdx)
			if(childIdx === -1) break;
			
			const p = this.heap[parentIdx]
			const c = this.heap[childIdx]
		
			if(p.diff <= c.diff) break;
			
			this.heap[parentIdx] = this.heap[childIdx]
			this.heap[childIdx] = p
			parentIdx = childIdx
		}
	}
	
	notEmpty(){
		return this.heap.length !== 0
	}
	
}

const getNeighbours = (arr, currPos) => {
	const [x, y] = currPos
	const neighbours = []
	if(x>0){
		neighbours.push([x-1, y])
	}
	if(x<arr.length-1){
		neighbours.push([x+1, y])
	}
	if(y>0){
		neighbours.push([x, y-1])
	}
	if(y<arr[0].length-1){
		neighbours.push([x, y+1])
	}
	
	return neighbours
}

const minimumEffortPath = (heights) => {
    if(heights.length === 1 && heights[0].length === 1) return 0
    const distances = [];
    for(let i = 0; i < heights.length; i++){
    	distances.push([]);
    	for(let j=0; j<heights[i].length; j++){
    		distances[i].push(Number.MAX_SAFE_INTEGER);
    	}
    }
    
    const pq = new PriorityQueue();
    pq.add(0, [0, 0]);
    let iter = 10;
    
    const addNeighbours = (curr, pq) => (neighbour, idx) => {
    		const [nx, ny] = neighbour;
    		const [cx, cy] = curr.idx;
    		const diff = Math.max(curr.diff, Math.abs(heights[cx][cy] - heights[nx][ny]) );
    		if(distances[nx][ny] <= diff) return;
    		pq.add(diff, [nx, ny]);
    		distances[nx][ny] = diff;
    		
    	};
    
    while(pq.notEmpty()){
    	const curr = pq.get();
    	const [cx, cy] = curr.idx;
    	
    	const neighbours = getNeighbours(heights, curr.idx);
    	neighbours.forEach(addNeighbours(curr, pq));
    }
    
    return (distances[distances.length-1][distances[0].length-1])
};