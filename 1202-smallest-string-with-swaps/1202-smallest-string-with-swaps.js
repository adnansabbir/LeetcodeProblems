class DisjointSet{
	constructor(size){
		this.parents = Array(size).fill(0).map((_,i)=> i)
	}
	
	find(i){
		this.parents[i] = this.parents[i] !== i ? this.find(this.parents[i]) : this.parents[i]
		return this.parents[i]
	}
	
	union(x, y){
		const xSet = this.find(x)
		const ySet = this.find(y)
		if(xSet === ySet) return
		
		this.parents[ySet] = xSet
	}
	
	getGroups(){
		this.parents.forEach((p, idx) => this.find(idx))
		
		const groups = {}
		this.parents
		.forEach((p, idx) => {
			if(p === idx) return
			
			if(groups[p] === undefined){
				groups[p] = [p]
			}
			groups[p].push(idx)
		})
		
		return groups
	}

}

const sortChars = (sArr, group) => {
	const selected = group.map(idx => sArr[idx])
	selected.sort()
	selected.forEach((val, idx) => sArr[group[idx]] = val)
}

const smallestStringWithSwaps = (s, pairs) =>  {
    const disjointSet = new DisjointSet(s.length)
	pairs.forEach(pair => {
		disjointSet.union(pair[0], pair[1])
	})
	
	const stringArr = s.split('')
	const groups = disjointSet.getGroups()
	Object.keys(groups).forEach(k => {
		groups[k].sort((a, b) => a-b)
		sortChars(stringArr, groups[k])
	})
	
	return stringArr.join('')
};