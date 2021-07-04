function solution(money, costs) {
  let answer = 0;
  let start = 0;
  let end = 0;
  let partialSum = 0;
  while (end < costs.length) {
    // console.log(start, end, partialSum);
    partialSum += costs[end];
    if (partialSum <= money) {
      answer = Math.max(answer, end - start + 1);
      end += 1;
    }
    if (partialSum > money) {
      partialSum -= costs[start];
      if (start === end) {
        start += 1;
        end += 1;
      } else {
        start += 1;
      }
    }
  }
  return answer;
}

let money = 500_000_000;
let cost = Array(500_000).fill(1000);
console.log(solution(money, cost));
// 500000;
money = 500;
cost = [499, 0, 0, 1, 2, 3, 4, 5];
console.log(solution(money, cost));
// 7
money = 50005000;
cost = Array.from(Array(10000), (_, i) => i + 1);
console.log(solution(money, cost));
// 10000

money = 49985001;
cost = Array.from(Array(10000), (_, i) => i + 1);
console.log(solution(money, cost));
// 9998

money = 49985000;
cost = Array.from(Array(10000), (_, i) => i + 1);
console.log(solution(money, cost));
//9997
//console.log(solution(1000, [1000, 0, 0, 0, 10001, 1, 2, 3]));
