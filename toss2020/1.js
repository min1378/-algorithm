function getMaskedName(name) {
  // 함수를 작성해주세요
  let temp = ""
  for (let i = 0; i < name.length - 2; i++) temp += "*"
  name = name.slice(0, 2) + temp
  return name
}

console.log(getMaskedName("KIM TO SU"))
