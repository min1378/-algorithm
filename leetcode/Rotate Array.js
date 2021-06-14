/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  const newNums = [];
  nums.forEach((num, index) => {
    newNums[index + k] = num;
  });
  const start = newNums.slice(nums.length, nums.length + k);
  const end = newNums.slice(k, nums.length);
  console.log(start, end);
  console.log(end, start);
  return [...start, ...end];
};
console.log(rotate([1, 2, 3, 4, 5, 6, 7], 3));
