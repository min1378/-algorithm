const solution = (prices) => {
  let beforePrice = prices[0];
  let downCount = 0;
  let upCount = 0;
  let direction = 0;
  const result = [];
  prices.forEach((price) => {
    if (beforePrice === price) {
      if (downCount !== 0 && upCount !== 0) result.push(direction * Math.min(downCount, upCount));
      downCount = 0;
      upCount = 0;
      direction = 0;
    }
    if (beforePrice < price) {
      if (direction === 1 && upCount !== 0) {
        result.push(Math.min(downCount, upCount));
        upCount = 0;
      }
      upCount += 1;
      direction = -1;
    }
    if (beforePrice > price) {
      if (direction === -1 && downCount !== 0) {
        result.push(-1 * Math.min(downCount, upCount));
        downCount = 0;
      }
      downCount += 1;
      direction = 1;
    }
    beforePrice = price;
  });
  if (direction === -1 && downCount !== 0) result.push(-1 * Math.min(downCount, upCount));
  if (direction === 1 && upCount !== 0) result.push(Math.min(downCount, upCount));
  console.log(result);
};
solution([12, 6, 6, 12, 6, 24, 30, 32, 34, 36, 24, 18, 6, 6, 18, 30, 6]);
solution([4, 3, 2, 1, 2, 3, 4, 3, 2, 1]);
solution([1000, 2000, 3000, 2000, 3000, 4000, 3000]);
