// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
  // write your code in JavaScript (Node.js 8.9.4)
  const NtoBinary = N.toString(2);
  const oneIndexList = [];
  for (let index = 0; index < NtoBinary.length; index++) {
    if (NtoBinary[index] === "1") {
      oneIndexList.push(index);
    }
  }
  console.log(oneIndexList);
  const result = oneIndexList.map((index, i) => oneIndexList[i + 1] - index - 1);
  console.log(result);

  return result[0];
}

solution(74901729);

function solution2(N) {
  const binary = N.toString(2);
  console.log(binary);
  const trimmed = binary.substr(0, binary.lastIndexOf("1") + 1);
  console.log(trimmed);
  return Math.max(...trimmed.split("1").map((item) => item.length));
}
console.log(solution2(74901729));
