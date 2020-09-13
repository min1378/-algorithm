function solution(cards) {
  let answer = 0
  let player = []
  let dealer = [] // 첫번째 카드는 안보임
  let index = 0
  let stop = false
  for (let i = 0; i < cards.length; i++) {
    var card = cards[i]
    if (card > 10) card = 10
    // 시작 두장 : 플레이어
    if (index === 0 || index === 2) {
      player.push(card)
      index += 1
      continue
    }
    // 시작 두장 : 딜러
    if (index === 1 || index === 3) {
      if (index === 1) {
        dealer.push(card)
        index += 1
        continue
      } else dealer.push(card)
      index += 1
    }
    const playerScore = newSum(player)
    const dealerScore = newSum(dealer)
    // console.log(i, stop, player, dealer, newMax(playerScore), newMax(dealerScore))
    // 블랙잭 상황
    if ((playerScore[0] === 21 || playerScore[1] === 21) && (dealerScore[0] === 21 || dealerScore[1] === 21)) {
      index = 0
      player = []
      dealer = []
      stop = false
      continue
    }
    if (playerScore[0] === 21 || playerScore[1] === 21) {
      answer += 3
      index = 0
      player = []
      dealer = []
      stop = false
      continue
    }
    if (dealerScore[0] === 21 || dealerScore[1] === 21) {
      answer -= 2
      index = 0
      player = []
      dealer = []
      stop = false
      continue
    }
    // 플레이어 21초과
    if (newMax(playerScore) === -1) {
      answer -= 2
      index = 0
      player = []
      dealer = []
      stop = false
      continue
    }
    // 딜러 21초과
    if (stop && newMax(dealerScore) === -1) {
      answer += 2
      index = 0
      player = []
      dealer = []
      stop = false
      continue
    }
    if (stop && newMax(dealerScore) > 16 && newMax(playerScore) === newMax(dealerScore)) {
      index = 0
      player = []
      dealer = []
      stop = false
      continue
    }
    if (stop && newMax(dealerScore) > 16 && newMax(playerScore) > newMax(dealerScore)) {
      answer += 2
      index = 0
      player = []
      dealer = []
      stop = false
      continue
    }
    if (stop && newMax(dealerScore) > 16 && newMax(playerScore) < newMax(dealerScore)) {
      answer -= 2
      index = 0
      player = []
      dealer = []
      stop = false
      continue
    }
    // index > 3일때,
    if (dealer[1] === 1 || dealer[1] > 6) {
      if (playerScore[0] < 18 && playerScore[1] < 18) {
        if (index % 2 === 0) player.push(card)
        else dealer.push(card)
      } else {
        stop = true
        dealer.push(card)
      }
    } else if (dealer[1] === 4 || dealer[1] === 5 || dealer[1] === 6) {
      stop = true
      dealer.push(card)
    } else if (dealer[1] === 2 || dealer[1] === 3) {
      if (playerScore[0] < 13 && playerScore[1] < 13) {
        if (index % 2 === 0) player.push(card)
        else dealer.push(card)
      } else {
        stop = true
        dealer.push(card)
      }
    }
    index += 1
  }
  if (player.length < 2 || dealer.length < 2) {
    return answer
  }
  const playerScore = newSum(player)
  const dealerScore = newSum(dealer)
  console.log(stop, player, dealer, playerScore, newMax(playerScore), dealerScore, newMax(dealerScore))
  if (newMax(dealerScore) < 17) {
    return answer
  }
  if (playerScore[0] === 21 || playerScore[1] === 21) {
    answer += 3
  } else if (dealerScore[0] === 21 || dealerScore[1] === 21) {
    answer -= 2
  }
  // 플레이어 21초과
  else if (newMax(playerScore) === -1) {
    answer -= 2
  }
  // 딜러 21초과
  else if (stop && newMax(dealerScore) === -1) {
    answer += 2
  } else if (stop && newMax(playerScore) > newMax(dealerScore)) {
    answer += 2
  } else if (stop && newMax(playerScore) < newMax(dealerScore)) {
    answer -= 2
  }
  return answer
}
const newMax = (list) => {
  const first = list[0]
  const second = list[1]
  if (first > 21 && second > 21) return -1
  if (first > 21) return second
  if (second > 21) return first
  return Math.max(first, second)
}
const newSum = (list) => {
  if (list.indexOf(1) > -1) {
    const result = [list.reduce((a, b) => a + b), list.reduce((a, b) => a + b) + 10]
    return result
  }
  return [list.reduce((a, b) => a + b), -1]
}
console.log(solution([10, 13, 10, 1, 2, 3, 4, 5, 6, 2]))
