function solution(n, k, cmds) {
  const result = Array.from({ length: n }, (x, i) => i);
  let index = k;
  const deleteStack = [];
  const deleteCommand = () => {
    deleteStack.push(result[index]);
    result.splice(index, 1);
  };
  const undoCommand = () => {
    const undoIndex = deleteStack.pop();
    result.splice(undoIndex, 0, undoIndex);
  };
  const upCommand = (count) => {
    index -= Number(count);
  };
  const downCommand = (count) => {
    index += Number(count);
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
  while (deleteStack.length) {
    const undoIndex = deleteStack.pop();
    result.splice(undoIndex, 0, -1);
  }
  return result.map((el, index) => (el === -1 || el !== index ? "X" : "O")).join("");
}

console.log(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]));
