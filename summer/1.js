function solution(code, day, data) {
  const result = [];
  for (const info of data) {
    if (!isNeedData(info, code, day)) {
      continue;
    }
    const dataToMap = splitData(info);
    result.push(dataToMap);
  }
  result.sort((a, b) => {
    if (a.time < b.time) return -1;
    return 1;
  });

  const answer = result.map(({ price }) => Number(price));
  return answer;
}
const isNeedData = (str, code, day) => {
  if (str.indexOf(`time=${day}`) < 0) return false;
  if (str.indexOf(`code=${code}`) < 0) return false;
  return true;
};
const splitData = (str) => {
  const dataMap = {};
  const blankSplit = str.split(" ");
  for (const data of blankSplit) {
    const [name, value] = data.split("=");
    dataMap[name] = value;
  }
  return dataMap;
};

solution("012345", "20190620", [
  "price=80 code=987654 time=2019062113",
  "price=90 code=012345 time=2019062014",
  "price=120 code=987654 time=2019062010",
  "price=110 code=012345 time=2019062009",
  "price=95 code=012345 time=2019062111",
]);
