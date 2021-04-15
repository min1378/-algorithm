function solution(needs, r) {
  const robotMap = {};
  for (const need of needs) {
    for (const [index, part] of need.entries()) {
      if (!part) continue;
      if (!robotMap[index]) robotMap[index] = 1;
      else robotMap[index] += 1;
    }
  }
  const partCountList = Object.values(robotMap);
  partCountList.sort((a, b) => b - a);
  const answer = partCountList[r - 1];
  return answer;
}

solution(
  [
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1],
  ],
  2
);
