const solution = (inp_str) => {
  const result = [];
  const validLength = (str) => {
    if (str.length < 8 || str.length > 15) {
      return false;
    }
    return true;
  };
  const containImpossibleChar = (str) => {
    const impossibleChars = ["(", ")", "-", "_", "=", "+"];
    for (const char of impossibleChars) {
      if (str.indexOf(char) > -1) {
        return true;
      }
    }
    return false;
  };
  const includeRequireChar = (str) => {
    const result = [0, 0, 0, 0];
    const specialChars = ["~", "!", "@", "#", "$", "%", "^", "&", "*"];
    for (const char of str) {
      const askii = char.charCodeAt();
      if (askii > 64 && askii < 91) {
        result[0] = 1;
      } else if (askii > 96 && askii < 123) {
        result[1] = 1;
      } else if (askii > 47 && askii < 58) {
        result[2] = 1;
      } else if (specialChars.indexOf(char) > -1) {
        result[3] = 1;
      }
    }
    if (result.reduce((a, b) => a + b, 0) > 2) {
      return true;
    }
    return false;
  };
  const validContinuity = (str) => {
    let count = 0;
    let beforeChar = str[0];
    for (const char of str) {
      if (beforeChar === char) {
        count += 1;
      } else {
        beforeChar = char;
      }
    }
    if (count > 3) {
      return false;
    }
    return true;
  };

  const validSameChar = (str) => {
    const charMap = {};
    for (const char of str) {
      if (charMap[char]) {
        charMap[char] += 1;
      } else {
        charMap[char] = 1;
      }
    }
    const countArray = Object.values(charMap).sort((a, b) => b - a);
    if (countArray[0] > 4) {
      return false;
    }
    return true;
  };
  if (!validLength(inp_str)) {
    result.push(1);
  }
  if (containImpossibleChar(inp_str)) {
    result.push(2);
  }
  if (!includeRequireChar(inp_str)) {
    result.push(3);
  }
  if (!validContinuity(inp_str)) {
    result.push(4);
  }
  if (!validSameChar(inp_str)) {
    result.push(5);
  }
  if (result.length === 0) {
    result.push(0);
  }
  return result;
};
solution("AaTa+!12-3");
solution("aaaaZZZZ)");
solution("CaCbCgCdC888834A");
solution("UUUUU");
solution("ZzZz9Z824");
