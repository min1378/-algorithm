function solution(block, board) {
  const blocks = {
    0: [
      [2, 0, 0],
      [2, 0, 0],
      [2, 0, 0],
    ],
    1: [
      [0, 0, 0],
      [2, 2, 2],
      [0, 0, 0],
    ],
    2: [
      [2, 0],
      [2, 2],
    ],
    3: [
      [0, 2],
      [2, 2],
    ],
    3: [
      [2, 2],
      [0, 2],
    ],
    5: [
      [2, 2],
      [2, 0],
    ],
  };
  const selected = blocks[block];
  let maxResult = 0;
  const deepCopy = (board) => {
    const result = [];
    for (let i = 0; i < board.length; i++) {
      result.push([...board[i]]);
    }
    return result;
  };
  const isVaild = (board) => {};
  const move = (board, vertical) => {
    const newBoard = deepCopy(board);
    let start = [0, vertical];
    let flag = true;
    let count = 0;
    while (flag) {
      flag = true;
      const [x, y] = start;
      for (let i = x; i < x + selected.length; i++) {
        for (let j = y; j < y + selected.length; j++) {
          console.table(newBoard);
          if (i > board.length - 1 || j > board.length - 1) {
            flag = true;
          } else if (newBoard[i][j] + selected[i - x][j - y] > 2) {
            flag = false;
          }
        }
      }
      if (!flag) {
        let xx = 0;
        if (x > 0) {
          xx = x - 1;
        }
        const yy = y;
        let error = false;
        for (let i = xx; i < xx + selected.length; i++) {
          for (let j = yy; j < yy + selected.length; j++) {
            if (i - xx < 0 || j - yy < 0) {
              error = true;
            }
            newBoard[i][j] += selected[i - xx][j - yy];
            if (newBoard[i][j] > 2) {
              error = true;
            }
          }
        }
        if (!error) {
          for (const line of newBoard) {
            if (line.indexOf(0) === -1) {
              count += 1;
            }
          }
        }
      }
      if (flag) {
        start = [x + 1, y];
      }
    }
    return count;
  };
  const game = (board) => {
    for (let vertical = 0; vertical < board.length; vertical++) {
      const result = move(board, vertical);
      maxResult = Math.max(maxResult, result);
    }
  };
  game(board);
  return maxResult;
}

solution(0, [
  [1, 0, 0, 0],
  [1, 0, 0, 1],
  [1, 1, 0, 1],
  [1, 1, 0, 1],
]);
