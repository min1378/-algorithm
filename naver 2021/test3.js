/* 엄격한 평가 */

var mi = 0

var fi = 0

_.go(
  _.range(100),

  _.map(function (val) {
    ++mi // 100번 루프

    return val * val
  }),

  _.filter(function (val) {
    ++fi // 100번 루프

    return val % 2
  }),

  _.take(5), // 5개 꺼내기

  console.log
)

console.log(mi, fi) // 100 100

/* 지연 평가로 성능 높이기 */

/* take(5) 에서 5개를 가져오는데 필요한만큼만 루프를 돈다 */

/* 하나를 제곱하면 바로 다음 필터에 넣어보고, true로 평가되면 take에 넣어서 하나를 축적,

   5개가 축적될 때 까지 반복한다 */

var mi = 0

var fi = 0

_.go(
  _.range(100),

  L.map(function (val) {
    ++mi // 10번 루프

    return val * val
  }),

  L.filter(function (val) {
    ++fi // 10번 루프

    return val % 2
  }),

  L.take(5),

  console.log
)

console.log(mi, fi) // 10 10
