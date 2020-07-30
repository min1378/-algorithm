// function printAgeGroup(age) {
//   if (age < 10) return "10대 미만"
//   else if (age > 90) return "90대 이상"
//   else return (age / 10).toString().split(".")[0] + "0대"
// }
function printAgeGroup(age) {
  if (age < 10) return "10대 미만"
  else if (age >= 90) return "90대 이상"
  else return (Math.round(age / 10) * 10).toString() + "대"
}
console.log(printAgeGroup(72))
