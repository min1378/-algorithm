function solution(N, number) {
  let answer = -1;
  if (N === number) return 1;
  const fiveNumberCaseList = Array.from({ length: 8 }, () => []);
  fiveNumberCaseList.map((array, index) => array.push(N * (index + 1)));

  for (let i = 1; i < 9; i++) {
    for (let j = 0; j < i; j++) {
      for (const firstNumber of fiveNumberCaseList[j]) {
        for (const secondNumber of fiveNumberCaseList[i - j - 1]) {
          fiveNumberCaseList[i].push(firstNumber + secondNumber);
          fiveNumberCaseList[i].push(firstNumber - secondNumber);
          fiveNumberCaseList[i].push(firstNumber * secondNumber);
          if (secondNumber !== 0) {
            fiveNumberCaseList[i].push(parseInt(firstNumber / secondNumber));
          }
        }
      }
    }
    if (fiveNumberCaseList[i].indexOf(number) > -1) {
      console.log(fiveNumberCaseList);
      answer = i + 1;
      return answer;
    }
  }
  console.log(fiveNumberCaseList);
  return answer;
}

console.log(solution(5, 12));
