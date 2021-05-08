const solution = (weights, head2head) => {
  const result = weights.reduce((prev, weight, index) => {
    const headList = head2head[index].split("");
    const winCount = headList.filter((result) => result === "W").length;
    const winningPercent = (winCount / (headList.length - 1)) * 100;
    const winOverWeightCount = headList.filter((result, index) => result === "W" && weights[index] > weight).length;
    prev.push({ index: index + 1, winningPercent, weight, winOverWeightCount });
    return prev;
  }, []);
  result.sort((a, b) => {
    if (a.winningPercent > b.winningPercent) return -1;
    if (a.winningPercent < b.winningPercent) return 1;
    if (a.winOverWeightCount > b.winOverWeightCount) return -1;
    if (a.winOverWeightCount < b.winOverWeightCount) return 1;
    if (a.weight > b.weight) return -1;
    if (a.weight < b.weight) return 1;
    if (a.index < b.index) return -1;
    if (a.index > b.index) return 1;
  });
  const answer = result.map(({ index }) => index);
  console.log(answer);
};

solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]);
solution([145, 92, 86], ["NLW", "WNL", "LWN"]);
solution([60, 70, 60], ["NNN", "NNN", "NNN"]);
