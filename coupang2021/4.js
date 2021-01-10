function solution(depar, hub, dest, roads) {
  var answer = -1
  let deparToHub = 0
  let hubToDest = 0
  const adjMap = {}
  for (const road of roads) {
    if (adjMap[road[0]]) adjMap[road[0]].push(road[1])
    else adjMap[road[0]] = [road[1]]
  }
  console.log(adjMap)
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
