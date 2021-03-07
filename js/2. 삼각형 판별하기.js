const solution = (a, b, c) => {
  const list = [a, b, c];
  let max = 0;
  let maxIndex = -1;
  for (let i = 0; i < list.length; i++) {
    if (max < list[i]) {
      max = list[i];
      maxIndex = i;
    }
  }
  const result = a + b + c - max > max ? "YES" : "NO";
  console.log(result);
  return result;
};

solution(6, 7, 11);
solution(13, 33, 17);
