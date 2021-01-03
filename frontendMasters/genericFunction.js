const memoize = (cb) => {
  let cache = {};
  return (n) => {
    if (n in cache) {
      return cache[n];
    }
    let result = cb(n);
    cache[n] = result;
    return result;
  };
};

const times10 = (n) => 10 * n;
const times5 = (n) => 5 * n;
const memoizedTimes10 = memoize(times10);
console.log(memoizedTimes10(8));
console.log(memoizedTimes10(7));
console.log(memoizedTimes10(6));
console.log(memoizedTimes10(5));
console.log(memoizedTimes10(4));
console.log(memoizedTimes10(3));
console.log(memoizedTimes10(8));
console.log(memoizedTimes10(7));
console.log(memoizedTimes10(6));
console.log(memoizedTimes10(5));
console.log(memoizedTimes10(4));
console.log(memoizedTimes10(3));
