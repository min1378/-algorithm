function solution(next_student) {
  let dp = Array(next_student.length).fill(0);
  let visited = Array(next_student.length + 1).fill(0);
  next_student = [0].concat(next_student);
  function dfs(curr, start) {
    console.log("현재", curr, "시작", start);
    if (next_student[curr] === 0) {
      dp[curr] = 1;
      return dp[curr];
    }
    if (visited[curr]) {
      if (start === next_student[curr]) {
        dp[curr] += 1;
      }
      return dp[curr];
    }
    visited[curr] = 1;
    dp[curr] = dfs(next_student[curr], start) + 1;
    return dp[curr];
  }
  for (let i = 1; i < next_student.length; i++) {
    dfs(i, i);
  }
  let maxValue = 0;
  console.log(dp);
  let idx = -1;
  for (let i = 1; i < dp.length; i++) {
    if (maxValue <= dp[i]) {
      maxValue = dp[i];
      idx = i;
    }
  }

  return idx;
}

console.log(solution([2, 3, 4, 5, 2]));
