var sumOfUnique = function (nums) {
  const countNum = new Array(101).fill(0);
  return nums
    .map((number) => {
      countNum[number] += 1;
      return number;
    })
    .filter((number) => countNum[number] === 1)
    .reduce((sum, num) => sum + num, 0);
};
sumOfUnique([10]);
