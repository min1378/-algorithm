function commaizeNumber(num) {
  let strNum = num.toString()
  let answer = ""
  let j = strNum.length
  for (let i = 0; i < strNum.length; i++) {
    if (i != 0 && j % 3 === 0) answer += ","
    answer += strNum[i]
    j--
  }
  return answer
}

console.log(commaizeNumber(123456789))
