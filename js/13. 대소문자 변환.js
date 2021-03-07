const solution = (string) => {
  let result = "";
  for (const char of string) {
    if (char === char.toUpperCase()) {
      result += char.toLowerCase();
    } else {
      result += char.toUpperCase();
    }
  }
  console.log(result);
  return result;
};

solution("stuDY");
