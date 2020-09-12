function solution(new_id) {
  if (validate(new_id)) return new_id
  new_id = new_id.toLowerCase() // 소문자
  const regExp = /[\{\}\[\]\/?,;:|\)*~`!^\+<>@\#$%&\\\=\(\'\"]/gi
  if (regExp.test(new_id)) new_id = new_id.replace(regExp, "")
  new_id = new_id.replace(/[.]{2,}/g, ".")
  if (new_id[0] === ".") new_id = new_id.substr(1)
  if (new_id[new_id.length - 1] === ".") new_id = new_id.substr(0, new_id.length - 1)
  if (new_id === "") new_id = "a"
  if (new_id.length > 15) new_id = new_id.slice(0, 15)
  if (new_id[new_id.length - 1] === ".") new_id = new_id.substr(0, new_id.length - 1)
  if (new_id.length < 3) {
    const length = new_id.length
    const str = new_id[length - 1]
    for (let i = 0; i < 3 - length; i++) {
      new_id += str
    }
  }
  return new_id
}

const validate = (userId) => {
  const pattern = /^[a-z0-9-_.]{3,15}$/
  if (!pattern.test(userId)) return false
  if (userId.includes("..") || userId[0] === "." || userId[userId.length - 1] === ".") return false
  return true
}

console.log(solution("abcdefghijklmn.p"))
