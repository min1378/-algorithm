function solution(penter, pexit, pescape, data) {
  var answer = ""
  const dataList = []
  const length = penter.length
  for (let i = 0; i < data.length; i = i + length) {
    const splitData = data.substring(i, i + length)
    dataList.push(splitData)
  }

  const result = dataList.reduce((prev, current, index) => {
    if (current === penter || current === pexit || current === pescape) return prev + pescape + current
    return prev + current
  }, "")
  answer = penter + result + pexit
  return answer
}

solution("1100", "0010", "1001", "1101100100101111001111000000")
