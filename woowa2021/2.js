function solution(s, op) {
  var answer = []
  for (let i = 1; i < s.length; i++) {
    const first = Number(s.substring(0, i))
    const second = Number(s.substring(i, s.length))
    if (op === "+") answer.push(first + second)
    else if (op === "-") answer.push(first - second)
    else if (op === "*") answer.push(first * second)
  }
  return answer
}

solution("1234", "+")
solution("987987", "-")
solution("31402", "*")
