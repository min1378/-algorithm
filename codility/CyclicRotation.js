function solution(A, K) {
  // write your code in JavaScript (Node.js 8.9.4)
  const quotiant = A.length;
  const reminder = K % quotiant;

  const result = Array.from({ length: quotiant }, () => 0);
  for (let i = 0; i < quotiant; i++) {
    const newIndex = (i + reminder) % quotiant;
    console.log(newIndex, i);
    result[newIndex] = A[i];
  }
  return result;
}
solution([3, 8, 9, 7, 6], 3);
