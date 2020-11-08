function solution(grades, weights, threshold) {
  const gradeWeightMap = {
    "A+": 10,
    A0: 9,
    "B+": 8,
    B0: 7,
    "C+": 6,
    C0: 5,
    "D+": 4,
    D0: 3,
    F: 0,
  }
  const result = grades.reduce((prev, current, index) => {
    const score = gradeWeightMap[current] * weights[index]
    return prev + score
  }, -1 * threshold)
  return result
}

solution(["A+", "D+", "F", "C0"], [2, 5, 10, 3], 50)
solution(["B+", "A0", "C+"], [6, 7, 8], 200)
