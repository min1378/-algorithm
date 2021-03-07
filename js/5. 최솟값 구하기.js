const solution = (list) => {
  let result = Number.MAX_SAFE_INTEGER; // list[0] 가능
  // 내장함수
  // Math.min(...list)
  // Math.min.apply(null, list)
  for (let i = 0; i < list.length; i++) {
    if (result > list[i]) {
      result = list[i];
    }
  }
  console.log(result);
  return result;
};
solution([5, 3, 7, 11, 2, 15, 17]);
