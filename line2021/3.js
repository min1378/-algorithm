function solution(n) {
  let string = n.toString()
  var answer = [99999999999, 0] // 숫자, count
  const splitAndPlus = (newString, count) => {
    if (count > answer[0]) return

    if (newString.length === 1) {
      answer[0] = count
      answer[1] = Number(newString)
      return
    }
    for (let i = 0; i < newString.length - 1; i++) {
      const first = newString.substr(0, i + 1)
      const second = newString.substr(i + 1, newString.length - i - 1)
      if (Number(first).toString().length == first.length && Number(second).toString().length == second.length) {
        const nextString = (Number(first) + Number(second)).toString()
        splitAndPlus(nextString, count + 1)
      }
    }
  }
  splitAndPlus(string, 0)
  return answer
}

console.log(solution(73425))
console.log(solution(10007))
console.log(solution(0))
console.log(solution(10007))
