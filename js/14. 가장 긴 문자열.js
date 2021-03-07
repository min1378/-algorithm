const solution = (array) => {
  let max = 0;
  let result = "";
  for (const string of array) {
    if (string.length > max) {
      max = string.length;
      result = string;
    }
  }
  console.log(result);
  return result;
};

solution(["teacher", "time", "student", "beautiful", "good"]);
