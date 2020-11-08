function solution(money, expected, actual) {
  var answer = -1
  let betAmount = 100
  answer = expected.reduce((prev, current, index) => {
    if (prev === 0) return 0
    if (current === actual[index]) {
      console.log(current, actual[index])
      const result = prev + betAmount
      betAmount = 100
      return result
    } else {
      const result = prev - betAmount
      betAmount *= 2
      if (result < betAmount) betAmount = result
      return result
    }
  }, money)
  return answer
}

solution(1200, ["T", "T", "H", "H", "H"], ["H", "H", "T", "H", "T"])
