function solution(places) {
  const answer = [];
  for (const place of places) {
    const seatList = extractLocation(place);
    const [result, underRangeList] = findUnderManhattanRange(seatList);
    if (!result) {
      answer.push(0);
      continue;
    }
    let flag = true;
    for (const couple of underRangeList) {
      const result = checkPartition(place, seatList, couple);
      if (!result) {
        answer.push(0);
        flag = false;
        break;
      }
    }
    if (flag) answer.push(1);
  }
  return answer;
}
const checkPartition = (place, seatList, couple) => {
  const [first, second] = couple;
  const [firstX, firstY] = seatList[first];
  const [secondX, secondY] = seatList[second];

  if (firstX === secondX || firstY === secondY) {
    const x = (firstX + secondX) / 2;
    const y = (firstY + secondY) / 2;
    if (place[x][y] === "X") return true;
    return false;
  }
  if (place[secondX][firstY] === "X" && place[firstX][secondY] === "X") return true;
  return false;
};

const extractLocation = (place) => {
  const seatList = [];
  let index = 0;
  for (let i = 0; i < place.length; i++) {
    for (let j = 0; j < place.length; j++) {
      if (place[i][j] === "P") {
        seatList.push([i, j]);
        index += 1;
      }
    }
  }
  return seatList;
};

const findUnderManhattanRange = (seatList) => {
  const result = [];
  for (let i = 0; i < seatList.length; i++) {
    for (let j = i + 1; j < seatList.length; j++) {
      const [firstX, firstY] = seatList[i];
      const [secondX, secondY] = seatList[j];
      const manhattanRange = Math.abs(firstX - secondX) + Math.abs(firstY - secondY);
      if (manhattanRange === 1) {
        return [false, result];
      }
      if (manhattanRange === 2) {
        result.push([i, j]);
      }
    }
  }
  return [true, result];
};

solution([
  ["PPPPP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
  ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]);
