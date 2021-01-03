const times10 = (n) => {};

const cache = {};
const factorial = (n) => {
  if (n in cache) {
    return cache[n];
  }
  let result = times10(n);
  cache[n] = result;
  return result;
};
