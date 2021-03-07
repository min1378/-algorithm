const solution = (string) => {
  let result = "";
  for (const char of string) {
    result += char.toUpperCase();
  }

  //string.toUpperCase();
  console.log(result);
  return result;
};

solution("ItisTimeToStudy");
