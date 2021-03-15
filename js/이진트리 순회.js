const solution = (n) => {
  let answer = "";
  const DFS = (v) => {
    if (v > 7) return;
    else {
      // 전위 순회
      console.log(v);
      DFS(v * 2);
      DFS(v * 2 + 1);
    }
  };
  DFS(n);
};
solution(1);
// 중위 순회
// else {
//   DFS(v * 2);
//   console.log(v);
//   DFS(v * 2 + 1);
// }

// 후위 순회
// else {
//   DFS(v * 2);
//   DFS(v * 2 + 1);
// console.log(v);
// }
