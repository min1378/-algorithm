function solution(w, h) {
  let answer = w * h
  
  const UnusableRectangle = w + h - calGcd(w, h)
  return answer - UnusableRectangle;
}
// 유클리드 최대 공약수
function calGcd(first, second) {
  if(second === 0){
      return first
  }
  return calGcd(second, first % second)
}