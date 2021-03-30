const lotto = () => {
  const lottoList = [];
  while (lottoList.length < 5) {
    const result = [];
    while (result.length < 6) {
      const number = Math.floor(Math.random() * 45) + 1;
      if (result.indexOf(number) === -1) {
        result.push(number);
      }
    }
    result.sort((a, b) => a - b);
    lottoList.push(result);
  }
  for (const lottoNumber of lottoList) {
    console.log(lottoNumber);
  }
};
lotto();
