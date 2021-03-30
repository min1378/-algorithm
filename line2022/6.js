function solution(program, flag_rules, commands) {
  const commandMap = {};
  // 룰에 따라 커맨드와 argument 타입을 맵에 담음.
  for (const flag_rule of flag_rules) {
    const [dashCommand, type] = flag_rule.split(" ");
    const [dash, command] = dashCommand.split("-");
    commandMap[command] = type;
  }

  // 프로그램이 유효한지 확인하는 함수.
  const validProgramName = (name) => program === name;

  // type이 NULL 일때 판단하는 함수.
  const validTypeNULL = (argumentList) => argumentList.length === 0;

  // argument가 알파벳 대소문자로 이루어져 있는지 확인하는 함수.
  const validTypeSTRING = (argument) => {
    // 소문자인지 확인하는 함수.
    const checkSmallLetter = (askii) => askii > 97 && askii < 123;
    // 대문자인지 확인하는  함수.
    const checkCapitalLetter = (askii) => askii > 64 && askii < 91;
    for (const char of argument) {
      const askii = char.charCodeAt();
      // 대문자나 소문자라면 패스.
      if (checkSmallLetter(askii) || checkCapitalLetter(askii)) {
        continue;
      } else {
        return false;
      }
    }
    return true;
  };
  const validTypeNUMBER = (argument) => {
    const checkNumber = (askii) => askii > 47 && askii < 58;
    for (const char of argument) {
      const askii = char.charCodeAt();
      if (!checkNumber(askii)) {
        return false;
      }
    }
    return true;
  };
  // 인자가 유효한지 확인하는 함수
  const validArgument = (command, argumentList) => {
    const type = commandMap[command];
    if (type === "STRINGS") {
      if (argumentList.lengh === 0) {
        return false;
      }
      for (const argument of argumentList) {
        if (!validTypeSTRING(argument)) {
          return false;
        }
      }
      return true;
    }
    if (type === "STRING") {
      // 인자가 없거나 한개 초과면 유효하지 않음.
      if (argumentList.length > 1 || argumentList.length === 0) {
        return false;
      }
      return validTypeSTRING(argumentList[0]);
    }
    if (type === "NUMBERS") {
      if (argumentList.length === 0) {
        return false;
      }
      for (const argument of argumentList) {
        if (!validTypeNUMBER(argument)) {
          return false;
        }
      }
      return true;
    }
    if (type === "NUMBER") {
      if (argumentList.length > 1 || argumentList.length === 0) {
        return false;
      }
      return validTypeNUMBER(argumentList[0]);
    }
    if (type === "NULL") {
      return validTypeNULL(argumentList);
    }
    return false;
  };
  const answer = [];
  for (const flag of commands) {
    const [name, ...restFlag] = flag.split(" ");

    // 프로그램 이름이 유효하지 않다면, false
    if (!validProgramName(name)) {
      answer.push(false);
      continue;
    }
    const commandAndArguments = restFlag.join(" ").trim().split("-");
    let unValidflag = false;
    for (const group of commandAndArguments) {
      if (group === "") {
        continue;
      }
      const [command, ...argumentList] = group.trim().split(" ");
      if (!validArgument(command, argumentList)) {
        unValidflag = true;
        break;
      }
    }
    if (unValidflag) {
      answer.push(false);
    } else {
      answer.push(true);
    }
  }
  return answer;
}

solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"], ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]); // [true, false]
solution("trip", ["-days NUMBERS", "-dest STRING"], ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]); // [false, true]
