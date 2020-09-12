function splitDutchPayAmount(peopleCount, amount) {
  let result = parseInt(amount / peopleCount)
  let remainder = amount % peopleCount
  let answer = []
  for (let i = 0; i < peopleCount; i++) answer.push(result)
  answer[0] += remainder
  return answer
}
