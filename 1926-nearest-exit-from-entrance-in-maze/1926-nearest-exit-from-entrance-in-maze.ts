function nearestExit(maze: string[][], entrance: number[]): number {
    let steps = 0
    const getNeighbors = (x: number, y: number): number[][] => {
        const result = [[x-1, y], [x+1,y],[x,y-1],[x,y+1]]
        return result.filter(([cx,cy]) =>
            cx >= 0 && cx < maze.length &&
            cy >= 0 && cy < maze[0].length &&
            maze[cx][cy] === '.')
    }

    const isAtExit = (x: number, y: number): boolean =>{
        if(x === entrance[0] && y === entrance[1]) return false
        return (x === 0 || x === maze.length - 1) || (y === 0 || y === maze[0].length - 1)
    }

    const queue = [entrance]
    maze[entrance[0]][entrance[1]] = '+'
    while(queue.length){
        const size = queue.length
        for(let i = 0; i<size; i++){
            const [cx, cy] = queue.shift()
            if(isAtExit(cx, cy)) return steps

            const neighbors = getNeighbors(cx, cy)
            neighbors.forEach(([x,y]) => maze[x][y] = '+')
            queue.push(...neighbors)
        }
        steps++
    }

    return -1
};