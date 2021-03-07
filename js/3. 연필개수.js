const solution = (n) => {
  const quotient = parseInt(n / 12);
  const reminder = n % 12;
  const result = reminder === 0 ? quotient : quotient + 1;
  console.log(result);
  return result;
};

solution(25);
solution(178);
