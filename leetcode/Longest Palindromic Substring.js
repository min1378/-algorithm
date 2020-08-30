
// /**
//  * @param {string} s
//  * @return {number}
//  */
const longestPalindrome = (s) =>{
  let startIndex = 0;
  let maxLength = 1;
  const expandAroundMiddle = (left, right) => {
    while (left >= 0 && right < s.length && s[left] === s[right]){
      const currentPalLength = right - left + 1
      if (currentPalLength > maxLength){
        maxLength = currentPalLength;
        startIndex = left;
      }
      left -= 1;
      right += 1
    }
  }
  for (let i = 0; i < s.length; i++) {
    expandAroundMiddle(i - 1, i + 1)
    expandAroundMiddle(i, i + 1)
  }
  return s.slice(startIndex, startIndex + maxLength)
};

// console.log(longestPalindrome("aaaa"))

// let longestPalindrome = s => {
//   let N = s.length;
//   if (!N) return '';
//   let ans = s[0];
//   let dp = [...Array(N)].map(row => Array(N).fill(false));
//   for (let j = 1; j < N; ++j) {
//       for (let i = j; i >= 0; --i) {
//           dp[i][j] = s[i] == s[j] && (j - i < 2 || dp[i + 1][j - 1]);
//           if (dp[i][j] && ans.length < j - i + 1)
//               ans = s.substring(i, j + 1); // +1 for i..j inclusive 🎯
//       }
//   }
  
//   return ans;
// };

// longestPalindrome("aaaa")