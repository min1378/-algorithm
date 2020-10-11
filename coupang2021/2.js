function solution(n, customers) {
  var answer = 0
  const days = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  const kiosks = Array.from({ length: n }, (v, i) => {
    return {
      serial: i,
      custom: [],
    }
  })
  let count = 0
  for (const customer of customers) {
    count += 1
    let flag = false
    const time = customer.split(" ")
    let [month, day] = time[0].split("/")
    month = Number(month)
    day = Number(day)
    const [hour, min, sec] = time[1].split(":")
    const spandTime = time[2]

    for (let i = 1; i < month + 1; i++) {
      day += days[i]
    }
    const newSeconds = day * 24 * 60 * 60 + Number(hour) * 60 * 60 + Number(min) * 60 + Number(sec) + Number(spandTime) * 60
    if (count < n + 1) {
      for (const kiosk of kiosks) {
        if (kiosk.custom.length === 0) {
          kiosk.custom.push(newSeconds)
          flag = true
          break
        }
      }
    }
    if (flag) continue
    let checkIndex = [-1, 0]
    for (let i = 0; i < kiosks.length; i++) {
      const lastTime = kiosks[i].custom[kiosks[i].custom.length - 1]
      if (lastTime <= newSeconds && checkIndex[1] <= newSeconds - lastTime) {
        checkIndex = [i, newSeconds - lastTime]
      }
    }
    kiosks[checkIndex[0]].custom.push(newSeconds)
  }

  for (let i = 0; i < kiosks.length; i++) {
    if (answer < kiosks[i].custom.length) answer = kiosks[i].custom.length
  }
  return answer
}

console.log(
  "answer",
  solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"])
)
console.log("answer", solution(2, ["02/28 23:59:00 03", "03/01 00:00:00 02", "03/01 00:05:00 01"]))
