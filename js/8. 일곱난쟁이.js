const getCombination = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]);
  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombination(rest, selectNumber - 1);
    const attached = combinations.map((combination) => [fixed, ...combination]);
    results.push(...attached);
  });
  return results;
};
const arraySum = (list) => {
  let result = 0;
  for (const number of list) {
    result += number;
  }
  return result;
};
const solution = (list) => {
  const combinations = getCombination(list, 7);
  for (const combination of combinations) {
    if (arraySum(combination) === 100) {
      console.log(combination);
      return combination;
    }
  }
};

solution([20, 7, 23, 19, 10, 15, 25, 8, 13]);
