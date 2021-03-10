const solution = (n, array) => {
  const scoreMap = {};
  for (let i = 0; i < array.length; i++) {
    if (scoreMap[array[i]]) {
      scoreMap[array[i]] += 1;
    } else {
      scoreMap[array[i]] = 1;
    }
  }
  const rankMap = {};
  let index = 0;
  for (const [key, value] of Object.entries(scoreMap)) {
    rankMap[key] = n - index - value + 1;
    index += value;
  }
  const result = [];
  for (let i = 0; i < array.length; i++) {
    result.push(rankMap[array[i]]);
  }
  console.log(result.join(" "));
  return result.join(" ");
};
solution(5, [87, 89, 92, 100, 76]);
