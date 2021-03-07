const solution = (list) => {
  const oddNumbers = [];
  for (const number of list) {
    if (number % 2 !== 0) {
      oddNumbers.push(number);
    }
  }
  const result = Math.min(...oddNumbers) || "없음.";
  console.log(result);
  return result;
};

solution([12, 77, 38, 41, 53, 92, 85]);
solution([12, 12, 12, 12, 12, 12, 12, 12, 12]); // Infinity
