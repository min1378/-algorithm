const cache = {};
const coins = [10, 6, 1];
const makeChange = (c) => {
  if (cache[c]) return cache[c];
  let minCoins = -1;

  coins.forEach((coin) => {
    if (c - coin >= 0) {
      let currMinCoins = makeChange(c - coin);
      if (minCoins === -1 || currMinCoins < minCoins) {
        minCoins = currMinCoins;
      }
    }
  });
};
