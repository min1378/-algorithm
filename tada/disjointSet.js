function main (numNodes, edges) {

  const parent = [];
  const rank = [];

  function makeSet (x) {
    parent[x] = x;
    rank[x] = 0;
  }

  function find (x) {
    if (x !== parent[x]) parent[x] = find(parent[x]);
    return parent[x];
  }

  function union (x, y) {
    const xRoot = find(x);
    const yRoot = find(y);
    
    if (xRoot === yRoot) {
      return false; // items were already in the same set
    }

    if (rank[xRoot] < rank[yRoot]) {
      parent[xRoot] = yRoot;
    } else if (rank[xRoot] > rank[yRoot]) {
      parent[yRoot] = xRoot;
    } else {
      parent[yRoot] = xRoot
      rank[xRoot] = rank[xRoot] + 1
    }

    return true; // items were not already in the same set
  }

  for (let node = 0; node < numNodes; node++) {
    makeSet(node);
  }

  for (let e = 0; e < edges.length; e++) {
    const [node1, node2] = edges[e];
    const didSomething = union(node1, node2);
  }
}