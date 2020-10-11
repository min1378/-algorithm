function solution(depar, hub, dest, roads) {
  var answer = -1
  let deparToHub = 0
  let hubToDest = 0
  const adjMap = {}
  for (const road of roads) {
    if (adjMap[road[0]]) adjMap[road[0]].push(road[1])
    else adjMap[road[0]] = [road[1]]
  }
  let stack = [depar]
  let checkMap = {}
  while (stack.length) {
    const start = stack.pop()
    console.log(stack)
    checkMap[start] = 1
    console.log(start, adjMap[start])
    if (start === hub) {
      deparToHub += 1
      continue
    }
    if (adjMap[start]) stack = stack.concat(adjMap[start])
  }
  stack = [hub]
  while (stack.length) {
    const start = stack.pop()
    if (start === dest) {
      hubToDest += 1
      continue
    }
    if (adjMap[start]) stack = stack.concat(adjMap[start])
  }
  return deparToHub * hubToDest
}

console.log(
  solution("SEOUL", "DAEGU", "YEOSU", [
    ["ULSAN", "BUSAN"],
    ["DAEJEON", "ULSAN"],
    ["DAEJEON", "GWANGJU"],
    ["SEOUL", "DAEJEON"],
    ["SEOUL", "ULSAN"],
    ["DAEJEON", "DAEGU"],
    ["GWANGJU", "BUSAN"],
    ["DAEGU", "GWANGJU"],
    ["DAEGU", "BUSAN"],
    ["ULSAN", "DAEGU"],
    ["GWANGJU", "YEOSU"],
    ["BUSAN", "YEOSU"],
  ])
)
function getRandomInt(min, max) {
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min)) + min //최댓값은 제외, 최솟값은 포함
}
const check = Array.from({ length: 100000 }, (v, i) => {
  return [getRandomInt(1, 10000), getRandomInt(1, 10000)].sort()
})
console.log(check)
console.log(solution(0, 2, 500, check))
