// function solution(food_times, k) {
//   var answer = 0
//   let sortArray = food_times
//     .map((e, i) => {
//       return { time: e, index: i + 1 }
//     })
//     .sort((a, b) => {
//       return a.time - b.time
//     })
//   console.log(sortArray)
//   return answer
// }
function solution(food_times, k) {
  var answer = 0
  var i = 0
  var t = 0
  const order = food_times
    .map((time, index) => {
      return { time, index }
    })
    .sort((a, b) => {
      if (a.time > b.time) return 1
      if (a.time < b.time) return -1
      if (a.index > b.index) return 1
      if (a.index < b.index) return -1
      return 0
    })
  while (k >= (order.length - i) * (order[i].time - t)) {
    k -= (order.length - i) * (order[i].time - t)
    t = order[i].time
    while (order[i].time - t <= 0) {
      order[i].time -= t
      if (order[++i] === undefined) return -1
    }
  }
  k = k % (order.length - i)
  for (let j = 0; j < i; j++) {
    if (order[j].index <= k) k++
  }
  return k + 1
}

for (let i = 1; i < 12; i++) {
  console.log(i, solution([4, 1, 1, 5], i))
}
