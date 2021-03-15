const solution = (n, array) => {
  let answer = 0;
  let diagonalSum = 0;
  let 
  for(let i = 0; i<n; i++){
    let horizonSum = 0;
    let verticalSum = 0;
    for(let j = 0; i<n; j++){
      horizonSum += array[i][j];
      verticalSum += array[j][i];
      // 대각선
      if(i === j){
        array[i][j]
      }
      if(i )
    }
  }
};
solution(5, [
  [10, 13, 10, 12, 15],
  [12, 39, 30, 23, 11],
  [11, 25, 50, 53, 15],
  [19, 27, 29, 37, 27],
  [19, 13, 30, 13, 19],
]);
