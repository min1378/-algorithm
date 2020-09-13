const string = "0123456"

for (let i = 0; i < string.length - 1; i++) {
  first = string.substr(0, i + 1)
  second = string.substr(i + 1, string.length - i - 1)
  console.log(first, Number(first).toString().length == first.length, second, Number(second).toString().length == second.length)
}
