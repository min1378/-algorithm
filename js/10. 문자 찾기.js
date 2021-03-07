const solution = (string, char) => {
  let result = 0;
  for (const character of string) {
    if (char === character) {
      result += 1;
    }
  }
  // string.split(char).length - 1;
  console.log(result);
  return result;
};

solution("COMPUTERPROGRAMMING", "R");
