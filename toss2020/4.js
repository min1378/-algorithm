// function formatToKoreanNumber(num) {
//   let strNum = num.toString()
//   let strArray = []
//   let remainder = strNum.length % 4
//   if (remainder != 0) strArray.push(strNum.slice(0, remainder))
//   for (let i = remainder; i < strNum.length; i += 4) strArray.push(strNum.slice(i, i + 4))

//   let koreanDegree = ["만", "억", "조"]
//   for (let j = strArray.length; j > -1; j--) {
//     if(strArray[j])
//   }
//   console.log(strArray)
//   return num
// }
// formatToKoreanNumber(10000)
function addComma(string) {
  return string.slice(0, 1) + "," + string.slice(1, 4)
}
function formatToKoreanNumber(num) {
  let answer = ""
  const hm = 10 ** 8
  const tt = 10 ** 4
  let is8 = Math.floor(num / hm)
  console.log(is8)
  if (is8) {
    let is8String = is8.toString()
    if (is8String.length == 4) is8String = addComma(is8String)
    answer += is8String + "억 "
  }
  num = num % hm

  let is4 = Math.floor(num / tt)
  if (is4) {
    let is4String = is4.toString()
    if (is4String.length == 4) is4String = addComma(is4String)
    answer += is4String + "만 "
  }
  num = num % tt
  let is0 = num
  if (is0) {
    let is0String = is0.toString()
    if (is0String.length == 4) is0String = addComma(is0String)
    answer += is0String
  }
  if (answer == "") return "0"
  return answer
}
console.log(formatToKoreanNumber(12))
