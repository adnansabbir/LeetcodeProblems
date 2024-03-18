function findMinArrowShots(points: number[][]): number {
    if(!points.length) return 0
    const pointsSorted = points.sort((a, b) => a[0] === b[0] ? b[1]-a[1] : a[0] - b[0])
    let totalShot = 1

    let left = points[0][0], right = points[0][1]
    for(let [start, end] of points){
        if(left>end || right < start){
            left = start
            right = end
            totalShot++
        }else{
            left = Math.max(left, start)
            right = Math.min(right, end)
        }
    }

    return totalShot
};