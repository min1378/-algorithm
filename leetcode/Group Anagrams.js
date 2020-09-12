/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const check = strs[0].sort().toString()
  for (const str of strs) {
    if (check !== str.sort().toString()) return false
  }
  return true
}
