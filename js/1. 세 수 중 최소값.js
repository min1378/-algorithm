const solution = (list) => {
  let result = 999;
  for (let i = 0; i < list.length; i++) {
    if (result > list[i]) {
      result = list[i];
    }
  }
  return result;
};
console.log(solution([1, 2, 3]));
