function solution(s) {
  let result = s;
  const numberList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
  for (let i = 0; i < numberList.length; i++) {
    const regexAll = new RegExp(numberList[i], "g");
    result = result.replace(regexAll, i);
  }
  return Number(result);
}
solution("oneoneoneoneoneone4seveneight");
