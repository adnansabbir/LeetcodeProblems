var isBipartite = function (graph) {
  let colorArr = new Array(graph.length).fill(-1);
  colorArr[0] = 1;
  let queue = [];
  for (let i = 0; i < graph.length; i++) {
    if (graph[i].length > 0) {
      queue.push(i);
    }
  }

  while (queue.length) {
    let top = queue.shift();
    let neighbors = graph[top];

    for (let node of neighbors) {
      // console.log("node is ",node);
      if (colorArr[node] === -1) {
        colorArr[node] = 1 - colorArr[top];
        queue.push(node);
      } else if (colorArr[node] === colorArr[top]) {
        return false;
      }
    }
  }
  // console.log(colorArr);
  return true;
};