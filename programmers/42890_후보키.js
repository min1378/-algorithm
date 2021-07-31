function solution(relation) {
  const subsets = getSubsets(Array.from({ length: relation[0].length }, (v, k) => k));
  const answer = [];
  subsets.sort((a, b) => {
    if (a.length > b.length) return 1;
    if (a.length === b.length) return 1;
    if (a.length < b.length) return -1;
  });
  for (const subset of subsets) {
    if (!checkminimized(subset, answer)) continue;
    if (checkSubset(subset, relation)) {
      answer.push(subset);
    }
  }
  return answer.length;
}
const getSubsets = (nums) => {
  const res = [];
  const dfs = (start = 0, arr = []) => {
    if (arr.length > 0) res.push(arr);
    for (let i = start; i < nums.length; i++) {
      dfs(i + 1, [...arr, nums[i]]);
    }
  };
  dfs();
  return res;
};
const checkminimized = (subset, answer) => {
  const isSubset = (superset, subset) => {
    let result = true;
    subset.forEach((el) => {
      if (!superset.has(el)) result = false;
    });
    return result;
  };
  for (const element of answer) {
    const setTarget = new Set(subset);
    const setElement = new Set(element);
    if (isSubset(setTarget, setElement)) return false;
    if (isSubset(setElement, setTarget)) return false;
  }
  return true;
};
const checkSubset = (subset, relation) => {
  const idMap = {};
  for (const row of relation) {
    let id = "";
    for (const index of subset) {
      const string = row[index].toString();
      id += string;
    }
    if (!idMap[id]) idMap[id] = true;
    else {
      return false;
    }
  }

  return true;
};
// solution([
//   ["100", "ryan", "music", "2"],
//   ["200", "apeach", "math", "2"],
//   ["300", "tube", "computer", "3"],
//   ["300", "con", "computer", "4"],
//   ["500", "muzi", "music", "3"],
//   ["600", "apeach", "music", "2"],
// ]);
solution([
  ["a", 1, "aaa", "c", "ng"],
  ["b", 1, "bbb", "c", "g"],
  ["c", 1, "aaa", "d", "ng"],
  ["d", 2, "bbb", "d", "ng"],
]);
