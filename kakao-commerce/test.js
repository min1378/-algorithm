let count = 0;
const check = () => {
  count += 1;
  check();
};
try {
  check();
} catch (e) {
  console.log("Maximum stack size is", count, "in your current browser");
}
