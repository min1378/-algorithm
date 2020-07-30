// function getAmount(text) {
//   res = text.replace(/[^0-9]/g, "")
//   return res
// }
function getAmount(text) {
  let answer = ""
  for (i = 0; i < text.length; i++) {
    if (!isNaN(Number(text[i]))) answer += text[i]
  }
  return answer
}
console.log(getAmount("$10,000원"))
