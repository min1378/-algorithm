var canChoose = function (groups, nums) {
  let count = 0;
  let startIndex = 0;
  for (const group of groups) {
    const [result, newStartIndex] = findGroup(group, nums, startIndex);
    if (!result) return false;
    startIndex = newStartIndex;
  }
  return true;
};
const findGroup = (group, nums, startIndex = 0) => {
  const head = group[0];
  const groupToString = group.toString();
  while (true) {
    const headIndex = nums.indexOf(head, startIndex);
    if (headIndex < 0) return [false, -1];
    const numsToString = nums.slice(headIndex, headIndex + group.length).toString();
    if (groupToString !== numsToString) startIndex = headIndex + 1;
    if (groupToString === numsToString) return [true, headIndex + group.length];
  }
};
console.log(canChoose([[21, 22, 21, 22, 21, 30]], [21, 22, 21, 22, 21, 22, 21, 30]));
