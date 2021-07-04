function solution(k, rates) {
  const object = {
    answer: k,
    standard: 0,
    buyStart: null,
  };
  rates.forEach((rate) => {
    const { answer, standard, buyStart } = object;
    // console.log(object, rate);
    if (!buyStart && answer < rate) {
    } else if (standard >= rate) {
      if (buyStart === null) {
        object["standard"] = rate;
        object["buyStart"] = rate;
      } else {
        object["answer"] += standard - buyStart;
        object["buyStart"] = rate;
        object["standard"] = rate;
      }
    } else if (standard < rate) {
      if (buyStart === null) {
        object["buyStart"] = rate;
        object["standard"] = rate;
      } else {
        object["standard"] = rate;
      }
    }
  });
  const { answer, standard, buyStart } = object;
  if (standard > buyStart) {
    object["answer"] += standard - buyStart;
  }
  return object["answer"];
}

const k2 = 1000;
const rates2 = [1000, 1200, 1200, 1000, 900, 1000, 1200, 1200];
console.log(solution(k2, rates2));
//2500001000
// solution(1000, [1200, 1000, 1100, 1200, 900, 1000, 1500, 900, 750, 1100]);
