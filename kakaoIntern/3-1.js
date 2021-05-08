function solution(n, k, cmds) {
  const result = Array.from({ length: n }, (x, i) => i);
  let index = k;
  const deleteStack = [];
  const deleteCommand = () => {
    deleteStack.push(result[index]);
    result[index] = -1;
    if (index === result.length - 1) {
      while (result[index] < 0) {
        index -= 1;
      }
    } else {
      const newIndex = result.slice(index + 1).find((value) => value > -1);
      if (newIndex === -1) {
        const otherIndex = result
          .slice(0, index)
          .reverse()
          .find((value) => value > -1);
        index = otherIndex;
      } else index = newIndex;
    }
  };
  const undoCommand = () => {
    const undoIndex = deleteStack.pop();
    result[undoIndex] = undoIndex;
  };
  const upCommand = (count) => {
    while (count > 0) {
      index -= 1;
      if (result[index] === -1) continue;
      count -= 1;
    }
  };
  const downCommand = (count) => {
    while (count > 0) {
      index += 1;
      if (result[index] === -1) continue;
      count -= 1;
    }
  };
  for (const cmd of cmds) {
    const [command, count] = cmd.split(" ");
    if (command === "C") {
      deleteCommand();
    }
    if (command === "Z") {
      undoCommand();
    }
    if (command === "U") {
      upCommand(count);
    }
    if (command === "D") {
      downCommand(count);
    }
  }
  return result.map((el, index) => (el === -1 || el !== index ? "X" : "O")).join("");
}

console.log(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]));
