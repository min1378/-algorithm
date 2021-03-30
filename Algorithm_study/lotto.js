const random = () => Math.floor(Math.random() * 45) + 1;
const randomPension = () => Math.floor(Math.random() * 999999) + 1;
const lotto = () => {
  const stack = [];
  while (stack.length < 6) {
    const number = random();
    if (stack.indexOf(number) > -1) continue;
    stack.push(number);
  }
  stack.sort((a, b) => a - b);
  console.log(stack);
};
lotto();
console.log(randomPension());
