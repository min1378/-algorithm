function solution(progresses, speeds) {
  let endDays = []
  for (let i = 0; i < progresses.length; i++) {
    let result = parseInt((100 - progresses[i]) / speeds[i])
    if ((100 - progresses[i]) % speeds[i]) result++
    endDays.push(result)
  }
  let answer = []
  let count = 0
  let standard = endDays[0]
  for (const endDay of endDays) {
    if (standard < endDay) {
      standard = endDay
      answer.push(count)
      count = 1
    } else count++
  }
  answer.push(count)

  return answer
}

console.log(solution([93, 30, 55], [1, 30, 5]))
