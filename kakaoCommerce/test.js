function solution(next_student) {
  const studentMap = {};
  const countMap = {};

  for (const [index, next] of next_student.entries()) {
    studentMap[index + 1] = next;
  }
  let max = [1, 0];
  for (let student = 1; student < next_student.length + 1; student++) {
    console.log(student, "시작");
    if (countMap[student]) {
      if (max[1] <= countMap[student]) {
        max = [student, countMap[student]];
      }
      console.log("패스");
      continue;
    }
    let count = 0;
    let startStudent = student;
    let orderList = [startStudent];
    let cycleIndex = -1;
    let memoIndex = -1;
    console.log(countMap);
    const visitedMap = {};
    visitedMap[startStudent] = 1;
    while (true) {
      count += 1;
      const nextStudent = studentMap[startStudent];
      console.log(nextStudent);
      if (nextStudent === 0) {
        break;
      }
      if (countMap[nextStudent]) {
        console.log("이미 다녀감", nextStudent);
        memoIndex = nextStudent;
        break;
      }
      // const twiceVisitedStudent = orderList.indexOf(nextStudent);
      if (visitedMap[nextStudent]) {
        console.log("사이클 발생", nextStudent);
        cycleIndex = visitedMap[nextStudent] - 1;
        break;
      }
      visitedMap[nextStudent] = count + 1;
      orderList.push(nextStudent);
      startStudent = nextStudent;
    }
    if (memoIndex > -1) {
      for (let index = 0; index < orderList.length; index++) {
        const student = orderList[index];
        countMap[student] = countMap[memoIndex] + count - index;
        if (max[1] <= countMap[student]) {
          max = [student, countMap[student]];
        }
      }
      continue;
    } else if (cycleIndex > -1) {
      for (let index = cycleIndex; index < orderList.length; index++) {
        const student = orderList[index];
        countMap[student] = orderList.length - cycleIndex;
        if (max[1] <= countMap[student]) {
          max = [student, countMap[student]];
        }
      }
      for (let index = 0; index < cycleIndex; index++) {
        const student = orderList[index];
        countMap[student] = count - index;
        if (max[1] <= countMap[student]) {
          max = [student, countMap[student]];
        }
      }
    } else {
      for (let index = 0; index < orderList.length; index++) {
        const student = orderList[index];
        countMap[student] = count - index;
        if (max[1] <= countMap[student]) {
          max = [student, countMap[student]];
        }
      }
    }
  }
  // const countList = Object.values(countMap);
  // let maxCount = 0;
  // let answer = -1;
  // for (const [index, count] of countList.entries()) {
  //   if (count >= maxCount) {
  //     maxCount = count;
  //     answer = index + 1;
  //   }
  // }
  console.log(max[0]);
  return max[0];
}

solution([5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2]);
//solution([6, 10, 8, 5, 8, 10, 5, 1, 6, 7]);
