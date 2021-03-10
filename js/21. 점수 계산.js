const solution = (n, array) => {
  let AdditionalPoint = 1;
  let result = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i]) {
      result += AdditionalPoint;
      AdditionalPoint += 1;
    } else {
      AdditionalPoint = 1;
    }
  }
  console.log(result);
  return result;
};

solution(10, [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]);
