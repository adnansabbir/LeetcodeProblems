function minMutation(start: string, end: string, bank: string[]): number {
    
    const getMutationCount = (gene1: string, gene2: string): number => {
        let result = 0
        for(let i = 0; i<gene1.length; i++){
            if(gene1[i] !== gene2[i]) result++
        }
        return result
    }
    
    const get1PhaseMutations = (gene: string, avoid: Set<string>): string[] => {
        return bank.filter((mutation) => !avoid.has(mutation) && getMutationCount(gene, mutation) === 1)
    }
    
    const queue = [start]
    let mutationCount = 0
    const checked = new Set<string>([start])
    while(queue.length){
        let size = queue.length
        for(let i = 0; i<size; i++){
            const curr = queue.shift()
            checked.add(curr)
            if(curr === end) return mutationCount
            queue.push(...get1PhaseMutations(curr, checked))
        }
        mutationCount++
    }
    
    return -1
};