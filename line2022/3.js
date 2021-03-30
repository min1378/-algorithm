const solution = (enter, leave) => {
  const result = Array.from({ length: enter.length + 1 }, () => 0);
  const enterList = [...enter];
  const leaveList = [...leave];
  const stack = [];
  stack.push(enterList.shift());
  while (leaveList.length > 0) {
    if (stack.indexOf(leaveList[0]) === -1) {
      for (const number of stack) {
        result[number] += 1;
      }
      const newNumber = enterList.shift();
      result[newNumber] += stack.length;
      stack.push(newNumber);
    } else {
      const index = stack.indexOf(leaveList[0]);
      leaveList.shift();
      stack.splice(index, 1);
    }
  }
  result.shift();
  return result;
};
solution([1, 3, 2], [1, 2, 3]);
solution([1, 4, 2, 3], [2, 1, 3, 4]);
solution([3, 2, 1], [2, 1, 3]);
solution([3, 2, 1], [1, 3, 2]);
solution([1, 4, 2, 3], [2, 1, 4, 3]);
