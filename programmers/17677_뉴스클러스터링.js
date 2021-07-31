function solution(str1, str2) {
  // 문자열 담는 맵
  const stringMap = {};
  // range(0, 5) => [0, 1, 2, 3, 4, 5];
  // str1에서 최대 999개 중복갯수가 나옴
  range(0, str1.length - 1).forEach((index) => {
    if (isAlphabet(str1[index]) && isAlphabet(str1[index + 1])) {
      // 문자열 2개를 stringMap에 넣음.
      const el = str1[index].toUpperCase() + str1[index + 1].toUpperCase();
      if (!stringMap[el]) stringMap[el] = 1;
      else stringMap[el] += 1;
    }
  });

  range(0, str2.length - 1).forEach((index) => {
    if (isAlphabet(str2[index]) && isAlphabet(str2[index + 1])) {
      const el = str2[index].toUpperCase() + str2[index + 1].toUpperCase();
      if (!stringMap[el]) stringMap[el] = 1000;
      else stringMap[el] += 1000;
    }
  });
  console.log(stringMap);
  const entries = Object.values(stringMap);
  const unionCount = entries.map((value) => countUnion(value)).reduce((sum, number) => sum + number, 0);
  const intersectionCount = entries.map((value) => countIntersection(value)).reduce((sum, number) => sum + number, 0);
  if (intersectionCount === 0 && unionCount === 0) return 65536;
  return Math.floor((intersectionCount / unionCount) * 65536);
}

function range(start, end) {
  return Array(end - start)
    .fill(0)
    .map((number, index) => number + index);
}
function isAlphabet(char) {
  const charUpper = char.toUpperCase();
  if (charUpper.charCodeAt(0) > 64 && charUpper.charCodeAt(0) < 91) return true;
  return false;
}
function countUnion(value) {
  const quote = parseInt(value / 1000);
  const rest = value % 1000;
  return Math.max(quote, rest);
}
function countIntersection(value) {
  const quote = parseInt(value / 1000);
  const rest = value % 1000;
  return Math.min(quote, rest);
}
solution("E=M*C^2", "e=m*c^2");
solution("aa1+aa2", "AAAA12");
solution("FRANCE", "french");
