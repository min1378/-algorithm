function solution(s) {
  let answer = 0;
  const stringArray = s.split("");

  for (let i = 0; i < s.length; i++) {
    const shallowArray = [...stringArray];
    const rotateString = arrayRotate(shallowArray, i).join("");
    if (checkBracket(rotateString)) answer += 1;
  }
  return answer;
}
function arrayRotate(arr, count) {
  count -= arr.length * Math.floor(count / arr.length);
  arr.push.apply(arr, arr.splice(0, count));
  return arr;
}
function checkBracket(strings) {
  const stack = [];
  const bracketMap = {
    "[": "]",
    "(": ")",
    "{": "}",
  };
  const closeBracketList = ["]", ")", "}"];

  for (const char of strings) {
    if (!stack.length) {
      if (closeBracketList.indexOf(char) > -1) return false;
      stack.push(char);
    } else if (bracketMap[stack[stack.length - 1]] === char) {
      stack.pop();
      continue;
    } else {
      stack.push(char);
    }
  }
  if (stack.length > 0) return false;
  return true;
}
solution("}]()[{");
