function solution(t, r) {
  const stack = [];
  const result = [];
  for (let i = 0; i < 10000; i++) {
    if (result.length === t.length) break;
    while (t.indexOf(i) > -1) {
      const index = t.indexOf(i);
      const dataMap = {
        index: index,
        order: t[index],
        grade: r[index],
      };
      stack.push(dataMap);
      t[index] = -1;
    }

    if (!stack.length) continue;
    stack.sort((a, b) => {
      if (a.grade < b.grade) return 1;
      if (a.grade > b.grade) return -1;
      if (a.order < b.order) return 1;
      if (a.order > b.order) return -1;
    });
    const passenger = stack.pop();
    result.push(passenger);
  }
  const answer = result.map(({ index }) => index);
  return answer;
}
solution([0, 1, 3, 0], [0, 1, 2, 3]);
