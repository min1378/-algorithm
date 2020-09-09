function solution(progresses, speeds) {
  let endDays = []
  for (let i = 0; i < progresses.length; i++) {
    let result = parseInt((100 - progresses[i]) / speeds[i]) // 몫
    if ((100 - progresses[i]) % speeds[i]) result++ // 나머지가 있을때 
    endDays.push(result)
  }
  let answer = []
  let count = 0
  let standard = endDays[0]
  console.log(endDays)
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