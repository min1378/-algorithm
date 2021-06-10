const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").toString().trim();
// const fs = require("fs");
// const inputs = fs.readFileSync("i10870.txt", "utf8").toString().trim().split("\n");
const solution = (n) => {
  const fiboMap = {};
  const fibo = (n) => {
    if (n <= 0) return 0;
    if (n === 1) return 1;
    if (fiboMap[n]) return fiboMap[n];
    fiboMap[n] = fibo(n - 2) + fibo(n - 1);
    return fiboMap[n];
  };
  console.log(fibo(n));
};
solution(Number(input));
// for (const input of inputs) {
//   solution(input);
// }
