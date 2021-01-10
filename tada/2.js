function solution(n, nationality) {
  const parentList = [-1];
  const rankList = [-1];
  for (let i = 1; i < n + 1; i++) {
    parentList[i] = i;
    rankList[i] = 0;
  }
  const findParent = (number) => {
    if (number !== parentList[number]) {
      parentList[number] = findParent(parentList[number]);
    }
    return parentList[number];
  };

  const union = (x, y) => {
    const xParent = findParent(x);
    const yParent = findParent(y);
    if (xParent === yParent) {
      return false;
    }
    if (rankList[xParent] < rankList[yParent]) {
      parentList[xParent] = yParent;
    }

    if (rankList[xParent] > rankList[yParent]) {
      parentList[yParent] = xParent;
    }

    if (rankList[xParent] === rankList[yParent]) {
      parentList[yParent] = xParent;
      rankList[xParent] = rankList[xParent] + 1;
    }

    return true;
  };
  for (let index = 0; index < nationality.length; index++) {
    const [node1, node2] = nationality[index];
    union(node1, node2);
  }
  let answer = 0;
  for (let i = 1; i < parentList.length; i++) {
    for (let j = i + 1; j < parentList.length; j++) {
      if (parentList[i] !== parentList[j]) {
        answer += 1;
      }
    }
  }
  return answer;
}
console.log(
  solution(5, [
    [1, 2],
    [2, 3],
  ])
);
