function solution(balls, orders) {
  const queue = []
  const answer = []
  let flag = false
  for (const order of orders) {
    const index = balls.indexOf(order)
    if (index === 0 || index === balls.length - 1) {
      flag = true
      balls.splice(index, 1)
      answer.push(order)
      while (flag) {
        if (queue.length === 0) {
          flag = false
          continue
        }
        if (queue.indexOf(balls[0]) > -1) {
          const item = balls[0]
          balls.splice(0, 1)
          answer.push(item)
          queue.splice(queue.indexOf(item), 1)
        } else if (queue.indexOf(balls[balls.length - 1]) > -1) {
          const item = balls[balls.length - 1]
          balls.splice(balls.length - 1, 1)
          answer.push(item)
          queue.splice(queue.indexOf(item), 1)
        } else flag = false
      }
    } else queue.push(order)
  }
  return answer
}

solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3])
