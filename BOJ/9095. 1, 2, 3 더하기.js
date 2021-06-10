// const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
const input = require("fs").readFileSync("i9095.txt").toString().trim().split("\n");
const [T, ...list] = input;

const solution = (n) => {
  const dpMap = {};
  let count = 0;
  const oneTwoThreeSum = (number) => {
    if (n === number) {
      count += 1;
      return;
    }
    if (n < number) return;
    oneTwoThreeSum(number + 1);
    oneTwoThreeSum(number + 2);
    oneTwoThreeSum(number + 3);
    return;
  };
  oneTwoThreeSum(0);
  console.log(count);
};

for (const data of list) {
  solution(Number(data));
}
