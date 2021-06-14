var tribonacci = function (n) {
  return trib(n, [0, 1, 1]);
};
if (12) {
}
function trib(n, dp) {
  console.log(dp);
  if (dp[n]) return dp[n];
  if (n == 0) return 0;
  if (n == 1) return 1;
  if (n == 2) return 1;

  dp[n] = trib(n - 1, dp) + trib(n - 2, dp) + trib(n - 3, dp);
  return dp[n];
}
console.log(tribonacci(10));
