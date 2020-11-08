function solution(logs) {
  var answer = []
  const studentMap = {}
  for (const log of logs) {
    const [id, problemNumber, score] = log.split(" ")
    if (!studentMap[id]) studentMap[id] = {}
    studentMap[id][problemNumber] = score
  }
  const entriesJson = Object.entries(studentMap)
  const cheatingSuspect = entriesJson.reduce((prev, current) => {
    const [id, solvedProblem] = current
    if (Object.keys(solvedProblem).length < 5) return prev
    const key = JSON.stringify(solvedProblem)
    if (!prev[key]) prev[key] = [id]
    else prev[key].push(id)
    return prev
  }, {})
  const cheatingList = Object.values(cheatingSuspect)
  for (const cheatingGroup of cheatingList) {
    if (cheatingGroup.length < 2) continue
    answer = answer.concat(cheatingGroup)
  }
  if (!answer.length) answer.push("None")
  return answer
}

solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"])
solution([
  "1901 1 100",
  "1901 2 100",
  "1901 4 100",
  "1901 7 100",
  "1901 8 100",
  "1902 2 100",
  "1902 1 100",
  "1902 7 100",
  "1902 4 100",
  "1902 8 100",
  "1903 8 100",
  "1903 7 100",
  "1903 4 100",
  "1903 2 100",
  "1903 1 100",
  "2001 1 100",
  "2001 2 100",
  "2001 4 100",
  "2001 7 95",
  "2001 9 100",
  "2002 1 95",
  "2002 2 100",
  "2002 4 100",
  "2002 7 100",
  "2002 9 100",
])
solution(["1901 10 50", "1909 10 50"])
