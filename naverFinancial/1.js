function solution(S) {
  // write your code in JavaScript (Node.js 8.9.4)
  const stringMap = {};
  for (const string of S) {
    if (stringMap[string]) {
      stringMap[string] += 1;
    }
    if (!stringMap[string]) {
      stringMap[string] = 1;
    }
  }
  const isSubstractable = (object) => object["B"] >= 1 && object["A"] >= 1 && object["L"] >= 2 && object["O"] >= 2 && object["N"] >= 1;
  let result = 0;
  while (isSubstractable(stringMap)) {
    result += 1;
    stringMap["B"] -= 1;
    stringMap["A"] -= 1;
    stringMap["L"] -= 2;
    stringMap["O"] -= 2;
    stringMap["N"] -= 1;
  }
  return result;
}

solution("BAONXXOLL");
solution("QAWABAWONL");
solution(
  "BALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOON"
);
solution(
  "BALLOONBALLASDASDASDOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOONBALLOON"
);
