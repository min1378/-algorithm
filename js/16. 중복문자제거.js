const solution = (string) => {
  const stringMap = {};
  let result = "";
  for (const char of string) {
    if (!stringMap[char]) {
      stringMap[char] = 1;
      result += char;
    }
  }
  // if(string.indexOf(char) === i) result += char;
  console.log(result);
  return result;
};

solution("ksekkset");
