const solution = (n) => {
  let answer = null;
  let visited = Array.from({ length: n + 1 }, () => 0);
  const DFS = (v) => {
    if (v === n + 1) {
      let temp = "";
      for (let i = 1; i <= n; i++) {
        if (visited[i] === 1) temp += i + " ";
      }
      console.log(temp);
    } else {
      visited[v] = 1;
      DFS(v + 1);
      visited[v] = 0;
      DFS(v + 1);
    }
  };
  DFS(1);
};

solution(3);
