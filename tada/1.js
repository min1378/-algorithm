const divideGroup = (adjList, start, end) => {
  const endIndex = adjList[start].indexOf(end);
  const startIndex = adjList[end].indexOf(start);
  adjList[start].splice(endIndex, 1);
  adjList[end].splice(startIndex, 1);
  return adjList;
};
const DFS = (n, adjList) => {
  const visited = Array.from({ length: n }, (v) => false);
  const stack = [0];
  const firstGroup = [0];

  while (stack.length > 0) {
    const start = stack.pop();
    visited[start] = true;
    const nodes = adjList[start];
    for (let i = 0; i < nodes.length; i++) {
      if (visited[nodes[i]]) continue;
      stack.push(nodes[i]);
      firstGroup.push(nodes[i]);
    }
  }
  const newStart = visited.indexOf(false);
  const secondGroup = [newStart];
  const secondStack = [newStart];
  while (secondStack.length > 0) {
    const start = secondStack.pop();
    visited[start] = true;
    const nodes = adjList[start];
    for (let i = 0; i < nodes.length; i++) {
      if (visited[nodes[i]]) continue;
      secondStack.push(nodes[i]);
      secondGroup.push(nodes[i]);
    }
  }
  return [firstGroup, secondGroup];
};
function solution(n, cars, links) {
  // 인접리스트
  const adjList = Array.from({ length: n }, (v) => []);
  for (const link of links) {
    const [start, end] = link;
    adjList[start - 1].push(end - 1);
    adjList[end - 1].push(start - 1);
  }
  let answer = 99999999;
  for (const link of links) {
    const [start, end] = link;
    const newAdjList = [];
    for (const line of adjList) {
      newAdjList.push([...line]);
    }
    const divideAdjList = divideGroup(newAdjList, start - 1, end - 1);
    const [first, second] = DFS(n, divideAdjList);
    let firstGroupSum = 0;
    for (const element of first) {
      firstGroupSum += cars[element];
    }
    let secondGroupSum = 0;
    for (const element of second) {
      secondGroupSum += cars[element];
    }
    if (answer > Math.abs(firstGroupSum - secondGroupSum)) {
      answer = Math.abs(firstGroupSum - secondGroupSum);
    }
  }
  return answer;
}

console.log(
  solution(
    6,
    [6, 4, 10, 9, 8, 4],
    [
      [4, 1],
      [3, 2],
      [1, 6],
      [3, 5],
      [5, 1],
    ]
  )
);
