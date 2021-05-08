function solution(k, num, links) {
  const N = num.length;
  const parent = Array(N).fill(-1);
  const lc = Array(N).fill(-1);
  const rc = Array(N).fill(-1);
  for (let i = 0; i < N; i++) {
    const [left, right] = links[i];
    lc[i] = left;
    rc[i] = right;
    if (left !== -1) parent[left] = i;
    if (right !== -1) parent[right] = i;
  }
  let root;
  for (let i = 1; i <= N; i++) {
    if (parent[i] === -1) {
      root = i;
      break;
    }
  }
  console.log(parent, lc, rc, root);
  var answer = 0;
  return answer;
}
solution(
  2,
  [6, 9, 7, 5],
  [
    [-1, -1],
    [-1, -1],
    [-1, 0],
    [2, 1],
  ]
);
// solution(
//   3,
//   [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
//   [
//     [-1, -1],
//     [-1, -1],
//     [-1, -1],
//     [-1, -1],
//     [8, 5],
//     [2, 10],
//     [3, 0],
//     [6, 1],
//     [11, -1],
//     [7, 4],
//     [-1, -1],
//     [-1, -1],
//   ]
// );
