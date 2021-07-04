function solution(lines) {
  const startResult = [];
  const endResult = [];
  for (const line of lines) {
    const [start, end] = lineSplitDate(line);
    startResult.push(start);
    endResult.push(end);
  }
  let answer = 0;
  for (let i = 0; i < startResult.length; i++) {
    const startTime = startResult[i];
    const oneSecStartTime = startTime - 999;
    const oneSecEndTime = startTime;

    let count = 0;
    for (let j = 0; j < startResult.length; j++) {
      const compareStartTime = startResult[j];
      const compareEndTime = endResult[j];
      if (
        (compareStartTime <= oneSecStartTime && compareEndTime >= oneSecEndTime) ||
        (compareStartTime >= oneSecStartTime && compareStartTime <= oneSecEndTime) ||
        (compareEndTime >= oneSecStartTime && compareEndTime <= oneSecEndTime)
      ) {
        count += 1;
      }
    }
    answer = Math.max(answer, count);
  }
  return answer;
}

const lineSplitDate = (line) => {
  const [date, time, T] = line.split(" ");
  const [hour, min, sec] = time.split(":");
  const [processSec, temp] = T.split("s");
  const startTime = hour * 60 * 60 * 1000 + min * 60 * 1000 + sec * 1000 - processSec * 1000 + 1;
  const endTime = hour * 60 * 60 * 1000 + min * 60 * 1000 + sec * 1000;
  return [startTime, endTime];
};

console.log(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]));
