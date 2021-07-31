function solution(n, t, m, timetable) {
  var answer = "";
  const compareTime = (firstTime, secondTime) => {
    const first = timeToMin(firstTime);
    const second = timeToMin(secondTime);
    if (first >= second) return true;
    else return false;
  };
  timetable.sort((a, b) => {
    if (compareTime(a, b)) {
      return 1;
    } else return -1;
  });
  const timeMap = {};
  for (const time of timetable) {
    if (timeMap[time]) timeMap[time] += 1;
    else timeMap[time] = 1;
  }
  const timeEntries = Object.entries(timeMap);
  let index = 0;
  let round = 0;
  let passengerCount = 0;
  while (round < n) {
    console.log(passengerCount, index, round);
    if (index === timeEntries.length) {
      round += 1;
      continue;
    }
    if (timeToMin(timeEntries[index][0]) <= 60 * 9 + (round + 1) * t) {
      passengerCount += timeEntries[index][1];
      if (passengerCount < m) {
        index += 1;
      } else if (passengerCount === m) {
        round += 1;
        passengerCount = 0;
        index += 1;
      } else {
        round += 1;
        timeEntries[index][1] = passengerCount - m;
        passengerCount = 0;
      }
    } else {
      round += 1;
      passengerCount = 0;
    }
  }
  if (index === 0 || passengerCount !== 0) {
    answer = minToTime(60 * 9 + (round - 1) * t);
  } else {
    answer = minToTime(timeToMin(timeEntries[index - 1][0]) - 1);
  }
  return answer;
}
const timeToMin = (time) => {
  const [hour, min] = time.split(":");
  return Number(hour) * 60 + Number(min);
};
const minToTime = (min) =>
  `${parseInt(min / 60)
    .toString()
    .padStart(2, "0")}:${(min % 60).toString().padStart(2, "0")}`;

// solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"], "09:00");
solution(2, 10, 2, ["09:10", "09:09", "08:00"], "09:09");
// solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"], "08:59");
// solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"], "00:00");
// solution(1, 1, 1, ["23:59"], "09:00");
// solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"], "18:00");
