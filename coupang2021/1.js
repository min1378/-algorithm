function solution(N) {
  var answer = [0, 0]
  for (let n = 10; n > 1; n--) {
    const changeToNBase = N.toString(n)
    const multipleAnswer = changeToNBase.split("").reduce((prev, current) => {
      if (current !== "0") return prev * Number(current)
      return prev
    }, 1)
    if (multipleAnswer > answer[1]) answer = [n, multipleAnswer]
  }
  return answer
}

console.log(solution(10))
console.log(solution(14))
