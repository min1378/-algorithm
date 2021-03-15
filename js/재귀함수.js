const solution = (n) => {
  const DFS = (L) => {
    if (L == 0) return;
    else {
      console.log(L);
      DFS(L - 1);
    }
  };
  DFS(n);
};

solution(3);
