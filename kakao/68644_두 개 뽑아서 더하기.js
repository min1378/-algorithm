function solution(numbers) {
  var answer = [];
  const numberMap = {};
  for(let i = 0; i< numbers.length; i++){
      for(let j = i + 1; j < numbers.length; j++){
          numberMap[numbers[i] + numbers[j]] = 1
      }
  }
  const check = Object.keys(numberMap)
  for(let i=0; i < check.length; i++){
      answer.push(Number(check[i]))
  }
  answer.sort((a, b) => a < b)
  return answer;
}