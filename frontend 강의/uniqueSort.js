const uniqueSort = (arr) => {
  const uniqueMap = {};
  const result = [];
  for (const element of arr) {
    if (!uniqueMap[element]) {
      result.push(element);
      uniqueMap[element] = true;
    }
  }
  return result.sort((a, b) => a - b);
};

console.log(uniqueSort([100, 100, 100, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2]));
