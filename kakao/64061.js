function solution(board, moves) {
  var answer = 0;
  let stack = [];
  let last_pick = Array.apply(null, new Array(board[0].length)).map(Number.prototype.valueOf, 0); // [0, 0, 0, 0, 0]
  for (var move = 0; move < moves.length; move++) {
    console.log(last_pick)
    const width = moves[move] - 1;
    for (var height = last_pick[width]; height < board.length; height++) {
      if (board[height][width] != 0) {
        if (stack[stack.length - 1] == board[height][width]) {
          answer += 2;
          stack.pop();
        } else {
          stack.push(board[height][width]);
        }
        last_pick[width] = height;
        board[height][width] = 0;
        break;
      }
    }
  }
  return answer;
}
console.log(
  solution(
    [
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3],
      [0, 2, 5, 0, 1],
      [4, 2, 4, 4, 2],
      [3, 5, 1, 3, 1],
    ],
    [1, 5, 3, 5, 1, 2, 1, 4]
  )
);
