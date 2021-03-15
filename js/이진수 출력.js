const solution = (n) => {
  let result = "";
  const DFS = (n) => {
    if (n === 0) return;
    else {
      DFS(parseInt(n / 2));
      result += String(n % 2);
    }
  };
  DFS(n);
  console.log(result);
};

solution(11);
