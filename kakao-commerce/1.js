function solution(giftCards, wants) {
  const giftCardMap = {};
  for (const giftCard of giftCards) {
    if (!giftCardMap[giftCard]) {
      giftCardMap[giftCard] = 1;
    } else giftCardMap[giftCard] += 1;
  }
  let answer = 0;
  for (const want of wants) {
    if (!giftCardMap[want]) {
      answer += 1;
    } else if (giftCardMap[want] === 0) {
      answer += 1;
    } else {
      giftCardMap[want] -= 1;
    }
  }
  return answer;
}

solution([4, 5, 3, 2, 1], [2, 4, 4, 5, 1]);
solution([5, 4, 5, 4, 5], [1, 2, 3, 5, 4]);
