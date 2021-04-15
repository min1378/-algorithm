function solution(absolutes, signs) {
  let answer = 0;
  for (const [index, number] of absolutes.entries()) {
    if (signs[index]) {
      answer += number;
    } else {
      answer -= number;
    }
  }
  return answer;
}
