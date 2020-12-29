function solution(n) {
  const threeBase = n.toString(3)
  const reversedThreeBase = threeBase.split("").reverse().join("")
  const answer = parseInt(reversedThreeBase, 3)
  console.log(answer)
  return answer;
}
solution(45)