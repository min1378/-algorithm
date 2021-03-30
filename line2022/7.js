function solution(program, flag_rules, commands) {
  const commandMap = {};
  const aliasMap = {};
  // 룰에 따라 커맨드와 argument 타입을 맵에 담음.
  for (const flag_rule of flag_rules) {
    const [dashCommand, ...restFlag] = flag_rule.split(" ");
    const [type, original] = restFlag;
    const [dash, command] = dashCommand.split("-");
    // 원본이 있다면, aliasMap에 원본을 등록한다.
    if (original) {
      const [dash, originalCommand] = original.split("-");
      aliasMap[command] = originalCommand;
    }
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
    // 유형이 ALIAS 라면, 원본을 찾아 다시 인자가 유효한지 확인한다.
    if (type === "ALIAS") {
      const originalCommand = aliasMap[command];
      return validArgument(originalCommand, argumentList);
    }
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
  // 원본 command를 찾는 함수.
  const findOriginalCommand = (command) => {
    // 별칭 object에서 원본을 찾아 반환.
    if (aliasMap[command]) {
      return aliasMap[command];
    }
    // 없다면, 원본이므로 그대로 반환.
    return command;
  };
  const answer = [];
  for (const flag of commands) {
    const [name, ...restFlag] = flag.split(" ");

    // 프로그램 이름이 유효하지 않다면, false
    if (!validProgramName(name)) {
      answer.push(false);
      continue;
    }
    // command 여부를 확인하는 Object.
    const commandCountMap = {};
    const commandAndArguments = restFlag.join(" ").trim().split("-");
    let unValidflag = false;
    for (const group of commandAndArguments) {
      if (group === "") {
        continue;
      }
      const [command, ...argumentList] = group.trim().split(" ");
      // 원본 command를 찾는다.
      const originalCommand = findOriginalCommand(command);
      // 이미 command가 사용되었다면, 잘못된 flag 이므로 에러 처리한다.
      if (commandCountMap[originalCommand]) {
        unValidflag = true;
        break;
      }
      commandCountMap[originalCommand] = 1;
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

solution("line", ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"], ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]); // [true, false]
solution("bank", ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"], ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]); // [false, false]
