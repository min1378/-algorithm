function solution(a, b) {
  let answer = 0;
  for(let i=0; i<a.length; i++){
    answer += a[i] * b[i]
  }
  return answer;
}

function solution(a, b) {
  return a.reduce((prev, current, i) => prev += a[i] * b[i], 0);
}