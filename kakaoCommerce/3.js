function solution(next_student) {
  const studentMap = {};
  const countMap = {};

  for (const [index, next] of next_student.entries()) {
    studentMap[index + 1] = next;
  }
  for (let student = 1; student < next_student.length + 1; student++) {
    if (countMap[student]) {
      continue;
    }
    let count = 0;
    let startStudent = student;
    let orderList = [startStudent];
    const visited = Array.from({ length: next_student.length + 1 }, (v) => false);
    visited[startStudent] = true;
    let cycleIndex = -1;
    let memoIndex = -1;
    console.log(countMap);
    console.log(student, "시작");
    while (true) {
      count += 1;
      const nextStudent = studentMap[startStudent];
      if (countMap[nextStudent]) {
        memoIndex = nextStudent;
        break;
      }
      if (nextStudent === 0) {
        break;
      }

      if (visited[nextStudent]) {
        const twiceVisitedStudent = orderList.indexOf(nextStudent);
        cycleIndex = twiceVisitedStudent;
        break;
      }
      visited[nextStudent] = true;
      orderList.push(nextStudent);
      startStudent = nextStudent;
    }
    if (memoIndex > -1) {
      for (let index = 0; index < orderList.length; index++) {
        const student = orderList[index];
        countMap[student] = countMap[memoIndex] + count - index;
      }
      continue;
    }
    if (cycleIndex > -1) {
      for (let index = cycleIndex; index < orderList.length; index++) {
        const student = orderList[index];
        countMap[student] = orderList.length - cycleIndex;
      }
      for (let index = 0; index < cycleIndex; index++) {
        const student = orderList[index];
        countMap[student] = count - index;
      }
    } else {
      for (let index = 0; index < orderList.length; index++) {
        const student = orderList[index];
        countMap[student] = count - index;
      }
    }
  }
  const countList = Object.values(countMap);
  let maxCount = 0;
  let answer = -1;
  for (const [index, count] of countList.entries()) {
    if (count >= maxCount) {
      maxCount = count;
      answer = index + 1;
    }
  }
  console.log(answer);
  return answer;
}

solution([5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2]);
//solution([6, 10, 8, 5, 8, 10, 5, 1, 6, 7]);
