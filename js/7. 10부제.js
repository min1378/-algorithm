const solution = (n, list) => {
  let count = 0;
  for (const number of list) {
    if (number % 10 === n) {
      count += 1;
    }
  }
  console.log(count);
  return count;
};

solution(3, [25, 23, 11, 47, 53, 17, 33]);
solution(0, [12, 20, 54, 30, 87, 91, 30]);
