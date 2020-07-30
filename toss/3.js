function calculate(type, operands) {
  if (type == "add") return operands.reduce((pre, next) => pre + next)
  else if (type == "multiply") return operands.reduce((pre, text) => pre * text)
}
