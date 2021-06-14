var numBusesToDestination = function (routes, source, target) {
  if (source == target) return 0;
  const graph = routes.map((x) => []);
  const sets = routes.map((x) => new Set(x));
  const sourceIndex = routes.length;
  const targetIndex = routes.length + 1;
  graph[sourceIndex] = [];
  graph[targetIndex] = [];
  for (let i = 0; i < routes.length; i++) {
    for (let j = i + 1; j < routes.length; j++) {
      if (hasJolt(routes[i], sets[j])) {
        graph[i].push(j);
        graph[j].push(i);
      }
    }
    if (sets[i].has(source)) graph[sourceIndex].push(i);
    if (sets[i].has(target)) graph[i].push(targetIndex);
  }
  return bfs(sourceIndex, targetIndex);

  function bfs(source, target) {
    const visited = routes.map((x) => false);
    const queue = [[source, 0]];
    visited[source] = true;

    while (queue.length) {
      let [cur, bus] = queue.shift();
      if (!graph[cur]) debugger;
      for (let i of graph[cur]) {
        if (!graph[cur].includes(i) || visited[i]) continue;
        if (i == target) return bus;
        queue.push([i, bus + 1]);
        visited[i] = true;
      }
    }
    return -1;
  }

  function hasJolt(r1 = [], r2 = new Set()) {
    let set = r2;
    for (let x of r1) {
      if (set.has(x)) return true;
    }
    return false;
  }
};
numBusesToDestination(
  [
    [1, 2, 7],
    [3, 6, 7],
  ],
  1,
  6
);
