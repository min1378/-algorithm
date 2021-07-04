/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function (n) {
  const dp = new Array(n + 1).fill(-1);
  dp[2] = 1;
  for (let i = 3; i < n - 1; i++) {
    for (let j = 1; j < i - 1; j++) {
      console.log("i: ", i, "j: ", j, i - j, dp[i - j] * j);
      dp[i] = Math.max(dp[i], Math.max(dp[i - j] * j, j * (i - j)));
    }
  }
  console.log(dp);
  return dp[n];
};
integerBreak(10);
