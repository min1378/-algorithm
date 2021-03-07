const solution = (string) => {
  // string.replace(/A/g, "#")
  return string.split("A").join("#");
};

console.log(solution("BANANA"));
