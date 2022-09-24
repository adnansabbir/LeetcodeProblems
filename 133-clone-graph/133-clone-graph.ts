/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     neighbors: Node[]
 *     constructor(val?: number, neighbors?: Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.neighbors = (neighbors===undefined ? [] : neighbors)
 *     }
 * }
 */

function cloneGraph(node: Node | null): Node | null {
    const realAndCloneNodeMap = new Map<Node, Node>()
	const getGraphClone = (node: Node | null): Node | null => {
        if(!node) return null
        if(realAndCloneNodeMap.has(node)) return realAndCloneNodeMap.get(node)
        
        const clonedNode = new Node(node.val)
        realAndCloneNodeMap.set(node, clonedNode)
        clonedNode.neighbors = node.neighbors.map(getGraphClone)
        
        return clonedNode
    }
    
    return getGraphClone(node)
};