const solution = (n, A, B) => {
  // 1 가위 2 바위 3 보
  const battle = (a, b) => {
    if (a === b) {
      return "D";
    }
    if ((a === 1 && b === 2) || (a === 2 && b === 3) || (a === 3 && b === 1)) {
      return "B";
    } else return "A";
  };
  const result = [];
  for (let i = 0; i < n; i++) {
    result.push(battle(A[i], B[i]));
  }
  console.log(result.join(" "));
  return result.join(" ");
};
solution(5, [2, 3, 3, 1, 3], [1, 1, 2, 2, 3]);
