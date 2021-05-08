const solution = (leave, day, holidays) => {
  var answer = -1;
  const satDays = calDate(day, "SAT");
  const sunDays = calDate(day, "SUN");
  const dayOffListSet = new Set([...holidays, ...satDays, ...sunDays]);
  const dayOffList = [...dayOffListSet];
  const calendar = Array.from({ length: 31 }, (x) => 0);
  dayOffList.map((day) => (calendar[day] = 1));
  const result = calLongestVacation(leave, calendar);
  console.log(result);
  return answer;
};
const calDate = (day, weekend) => {
  const days = ["NONE", "SAT", "FRI", "THU", "WED", "TUE", "MON", "SUN"];
  let startDay = -1;
  if (weekend === "SAT") startDay = days.indexOf(day);
  if (weekend === "SUN") startDay = (days.indexOf(day) + 1) % 7;
  const result = [];
  while (startDay <= 30) {
    result.push(startDay);
    startDay += 7;
  }
  return result;
};
const calLongestVacation = (leave, calendar) => {
  let maxResult = 0;
  const length = calendar.length;
  for (let i = 1; i < length; i++) {
    for (let j = i + 1; j < length; j++) {
      const sliceCalendar = calendar.slice(i, j + 1);
      const zeroCount = sliceCalendar.filter((el) => el === 0).length;
      if (i === 1 && j === 3) console.log(i, j, zeroCount, sliceCalendar, sliceCalendar.length);
      if (zeroCount <= leave) {
        maxResult = Math.max(maxResult, sliceCalendar.length);
      }
    }
  }
  return maxResult;
};
solution(4, "FRI", [6, 21, 23, 27, 28]);
// solution(3, "SUN", [2, 6, 17, 29]);
// solution(30, "MON", [1, 2, 3, 4, 28, 29, 30]);
