/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  let sCharsMap = {}
  let tCharsMap = {}
  for (const char1 of s) {
    if (sCharsMap[char1] >= 0) sCharsMap[char1] += 1
    else sCharsMap[char1] = 1
  }

  for (const char2 of t) {
    if (tCharsMap[char2] >= 0) tCharsMap[char2] += 1
    else tCharsMap[char2] = 1
  }
  for (const sChar in sCharsMap) {
    if (sCharsMap[sChar] !== tCharsMap[sChar]) return false
  }

  for (const tChar in tCharsMap) {
    if (sCharsMap[tChar] !== tCharsMap[tChar]) return false
  }
  return true
}

isAnagram("aa", "a")

const isAnagram = (s, t) => {
  if (s.length !== t.length) return false
  let sCharsMap = {}
  for (const char of s) {
    sCharsMap[char] = sCharsMap[char] + 1 || 1
  }

  for (const char2 of t) {
    if (tCharsMap[char2] >= 0) tCharsMap[char2] += 1
    else tCharsMap[char2] = 1
  }
  for (const sChar in sCharsMap) {
    if (sCharsMap[sChar] !== tCharsMap[sChar]) return false
  }

  for (const tChar in tCharsMap) {
    if (sCharsMap[tChar] !== tCharsMap[tChar]) return false
  }
  return true
}

isAnagram("aa", "a")
