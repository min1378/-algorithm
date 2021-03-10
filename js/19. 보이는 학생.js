const solution = (n, array) => {
  let maxValue = array[0];
  let count = 1;
  for (let i = 1; i < array.length; i++) {
    if (maxValue < array[i]) {
      maxValue = array[i];
      count += 1;
    }
  }
  console.log(count);
  return count;
};

solution(8, [130, 135, 148, 140, 145, 150, 150, 153]);
