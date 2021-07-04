const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

class PQ {
  constructor(size) {
    this.node = 1;
    this.tree = new Array(size + 1).fill(0);
  }

  push(val) {
    const { tree } = this;
    if (this.node >= tree.length) {
      console.log("overflow");
      return;
    }

    tree[this.node] = val;
    this.node += 1;
    let child = this.node - 1;

    while (child > 1) {
      const parent = Math.floor(child / 2);
      if (tree[child] < tree[parent]) {
        // 정렬 기준
        const temp = tree[child];
        tree[child] = tree[parent];
        tree[parent] = temp;
      } else {
        break;
      }
      child = parent;
    }
  }

  isEmpty() {
    return this.node <= 1;
  }

  pop() {
    const { tree } = this;
    if (this.node <= 1) {
      console.log("empty");
      return;
    }

    const popped = tree[1];
    tree[1] = tree[this.node - 1];
    this.node -= 1;
    let parent = 1;

    while (parent < this.node - 1) {
      let child = -1;
      if (parent * 2 >= this.node) {
        break;
      } else if (parent * 2 < this.node && parent * 2 + 1 >= this.node) {
        child = parent * 2;
      } else {
        if (tree[parent * 2] < tree[parent * 2 + 1]) {
          child = parent * 2;
        } else {
          child = parent * 2 + 1;
        }
      }

      if (tree[child] < tree[parent]) {
        const temp = tree[child];
        tree[child] = tree[parent];
        tree[parent] = temp;
        parent = child;
      } else {
        break;
      }
    }
    return popped;
  }
}

// n = node 수
// m = 단방향 간선 수
const [n, m] = input
  .shift()
  .split(" ")
  .map((str) => +str);
const graph = Array.from({ length: n + 1 }, () => []);
const inDegree = Array.from({ length: n + 1 }, () => 0);

// 노드 연결 및 진입 차수 기록
for (let i = 0; i < m; i++) {
  const [x, y] = input[i].split(" ").map((str) => +str);
  graph[x].push(y);
  inDegree[y] += 1;
}

// 진입 차수가 0인 노드를 pq에 push
const pq = new PQ(n);
for (let i = 1; i <= n; i++) {
  if (inDegree[i] === 0) pq.push(i);
}

const result = []; // pq에서 나온 노드의 순서를 저장

// pq가 빌때까지
while (!pq.isEmpty()) {
  const node = pq.pop(); // 집인 차수가 0인 node
  result.push(node);

  // 진입 차수가 0인 node의 간선 제거
  for (let i = 0; i < graph[node].length; i++) {
    const next = graph[node][i];
    inDegree[next] -= 1;

    // 간선이 제거된 다음 노드의 진입 차수가 0이 됐다면 pq에 push
    if (inDegree[next] === 0) {
      pq.push(next);
    }
  }
}

console.log(result.join(" "));
