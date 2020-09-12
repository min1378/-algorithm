// function getAge(birthDate, nowDate) {
//   let splitBirth = birthDate.split(" ")
//   let splitNow = nowDate.split(" ")
//   let splitBirth2 = splitBirth[0].split("-")
//   const monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
//   let birthToDate = splitBirth2[0] * 365 + monthDays[splitBirth2[1]]
//   console.log(splitBirth, splitNow)
//   return ""
// }
// getAge("1993-12-27 00:00:00", "2020-08-31 00:00:00")

function getAge(birthDate, nowDate) {
  let splitBirth = birthDate.split(" ")
  let splitBirth2 = splitBirth[0].split("-")
  let splitBirth3 = splitBirth[1].split(":")
  let splitNow = nowDate.split(" ")
  let splitNow2 = splitNow[0].split("-")
  let splitNow3 = splitNow[1].split(":")
  //console.log(splitBirth2, splitBirth3, splitNow2, splitNow3)
  let birth = new Date(Number(splitBirth2[0]), Number(splitBirth2[1]), Number(splitBirth2[2]), Number(splitBirth3[0]), Number(splitBirth3[1]), Number(splitBirth3[2]))
  //console.log(birth)
  let now = new Date(Number(splitNow2[0]), Number(splitNow2[1]), Number(splitNow2[2]), Number(splitNow3[0]), Number(splitNow3[1]), Number(splitNow3[2]))
  //console.log(now)
  let difftime = (now.getTime() - birth.getTime()) / (1000 * 60 * 60 * 24 * 365)
  if (difftime <= 0) return "만 0세, 한국나이 0세"
  let answer = "만 " + Math.floor(difftime).toString() + "세, 한국나이 " + (Math.ceil(difftime) + 1).toString() + "세"
  return answer
}

console.log(getAge("1993-12-27 00:00:00", "2020-08-31 00:00:00"))
