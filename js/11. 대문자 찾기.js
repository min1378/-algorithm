const solution = (string) => {
  let result = 0;
  for (const char of string) {
    if (char === char.toUpperCase()) {
      result += 1;
    }
  }
  // 아스키
  // 대문자: 65 ~ 90
  // char.charCodeAt(); 아스키 코드

  console.log(result);
  return result;
};

solution("KoreaTimeGood");
