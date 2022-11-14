function removeStones(stones: number[][]): number {
    const graphX: Record<number, number[]> = {}
    const graphY: Record<number, number[]> = {}

    // O(N) as I am going through all of the stones
    for(let [x,y] of stones){
        if(graphX[x] === undefined) graphX[x] = []
        if(graphY[y] === undefined) graphY[y] = []

        graphX[x].push(y)
        graphY[y].push(x)
    }

    let connectedStones = 0
    // O(n) memory as we have to store all the stones and store them on visited
    let visited = new Set<string>()

    // O(n*n)
    for(let [x,y] of stones){
        if(visited.has(`${x}-${y}`)) continue

        const queue = [[x,y]]

        while(queue.length){
            const size = queue.length
            for(let i = 0; i < size; i++){
                const [cx, cy] = queue.shift()
                if(visited.has(`${cx}-${cy}`)) continue
                visited.add(`${cx}-${cy}`)
                graphX[cx].forEach(y => queue.push([cx, y]))
                graphY[cy].forEach(x => queue.push([x, cy]))
            }
        }
        connectedStones++
    }
    return stones.length - connectedStones
};