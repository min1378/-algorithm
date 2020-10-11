function solution(k, score) {
  var answer = -1
  const diffMap = {}
  const deleteMap = {}
  const diffList = []
  for (let i = 1; i < score.length; i++) {
    const diff = score[i - 1] - score[i]
    diffList.push(diff)
    if (diffMap[diff] >= 0) diffMap[diff] += 1
    else diffMap[diff] = 1
  }
  for (let i = 0; i < diffList.length; i++) {
    const checkScore = diffList[i]
    if (diffMap[checkScore] >= k) {
      deleteMap[i] = 1
      deleteMap[i + 1] = 1
    }
  }
  answer = score.length - Object.keys(deleteMap).length
  return answer
}

console.log(solution(3, [24, 22, 20, 10, 5, 3, 2, 1]))
console.log(solution(3, [10, 9, 8, 7, 6, 5, 4, 1, 0]))
console.log(solution(2, [1300000000, 700000000, 668239490, 618239490, 568239490, 568239486, 518239486, 157658638, 157658634, 100000000, 100]))
