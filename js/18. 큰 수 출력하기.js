const solution = (n, array) => {
  let beforeNumber = array[0];
  const result = [array[0]];
  for (let i = 1; i < array.length; i++) {
    if (beforeNumber < array[i]) {
      result.push(array[i]);
    }
    beforeNumber = array[i];
  }
  console.log(result.join(" "));
  return result.join(" ");
};
solution(6, [7, 3, 9, 5, 6, 12]);
