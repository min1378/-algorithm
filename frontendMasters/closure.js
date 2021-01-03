const times10 = (n) => n * 10;

const memoizedClosureTimes10 = () => {
  let cache = {};
  return (n) => {
    if (n in cache) {
      return cache[n];
    }
    let result = n * 10;
    cache[n] = result;
    return result;
  };
};

const memoClosureTimes10 = memoizedClosureTimes10();
