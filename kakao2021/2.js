function solution(orders, course) {
  let popularOrders = {}
  for (const count of course) {
    const counterMaps = {}
    for (const order of orders) {
      const newOrder = order.split("").sort().join("")
      const orderCombinationList = getCombination(newOrder, count)
      for (const orderCombination of orderCombinationList) {
        if (counterMaps[orderCombination] >= 0) counterMaps[orderCombination] += 1
        else counterMaps[orderCombination] = 1
      }
    }
    popularOrders[count] = counterMaps
  }
  const answer = []

  for (const [key, values] of Object.entries(popularOrders)) {
    const max = Math.max(...Object.values(values))
    if (max < 2) continue
    for (const [menu, count] of Object.entries(values)) {
      if (count === max) answer.push(menu)
    }
  }
  return answer.sort()
}

const getCombination = (arr, m) => {
  const combinations = []
  const picked = []
  const used = []
  for (let i = 0; i < arr.length; i++) used.push(0)
  const find = (picked) => {
    if (picked.length === m) {
      const result = []
      for (let i of picked) {
        result.push(arr[i])
      }
      combinations.push(result.join(""))
      return
    } else {
      let start = picked.length ? picked[picked.length - 1] + 1 : 0
      for (let i = start; i < arr.length; i++) {
        if (i === 0 || arr[i] !== arr[i - 1] || used[i - 1]) {
          picked.push(i)
          used[i] = 1
          find(picked, m, combinations)
          picked.pop()
          used[i] = 0
        }
      }
    }
  }
  find(picked, m, combinations)
  return combinations
}

console.log(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
