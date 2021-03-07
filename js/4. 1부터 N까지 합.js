const solution = (n) => {
  let result = 0;
  for (let i = 1; i < n + 1; i++) {
    result += i;
  }
  console.log(result);
  return result;
};
solution(6);
solution(10);
