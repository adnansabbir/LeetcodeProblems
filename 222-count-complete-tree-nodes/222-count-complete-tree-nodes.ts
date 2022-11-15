function countNodes(root: TreeNode | null): number {
    if(!root) return 0

    const queue = [root]
    let total = 0
    while(queue.length){
        const size = queue.length
        for(let i = 0; i<size; i++){
            const node = queue.shift()
            total++
            if(node.left) queue.push(node.left)
            if(node.right) queue.push(node.right)
        }
    }

    return total
};