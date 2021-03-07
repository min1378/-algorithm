const solution = (string) => {
  const center = parseInt(string.length / 2);
  const reminder = string.length % 2;
  // const result = reminder === 0 ? string.substring(center - 1, center + 1) : string.substring(center, center + 1);
  const result = reminder === 0 ? string[center - 1] + string[center] : string[center];
  console.log(result);
  return result;
};

solution("study");
solution("time");
