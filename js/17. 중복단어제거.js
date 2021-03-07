const solution = (array) => {
  const stringMap = {};
  const result = [];
  for (const string of array) {
    if (!stringMap[string]) {
      stringMap[string] = 1;
      result.push(string);
    }
  }
  // const result = array.filter((string, i) => array.indexOf(string) === i);
  console.log(result);
  return result;
};

solution(["good", "time", "good", "time", "student"]);
