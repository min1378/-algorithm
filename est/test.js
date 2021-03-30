function longestChain(words) {
  // Write your code here
  const wordMap = {};
  words.sort((a, b) => {
    if (a.length > b.length) return 1;
  });
  for (const word of words) {
    let flag = false;
    let maxCount = 0;
    for (let i = word.length - 1; i > -1; i--) {
      const wordList = word.split("");
      wordList.splice(i, 1);
      const splitWord = wordList.join("");
      console.log(splitWord);
      if (wordMap[splitWord]) {
        flag = true;
        if (maxCount < wordMap[splitWord]) {
          maxCount = wordMap[splitWord];
        }
      } else {
        continue;
      }
    }
    wordMap[word] = maxCount + 1;
  }
  console.log(wordMap);
  const result = Object.values(wordMap);
  result.sort((a, b) => a - b);
  result;
}
longestChain(["a", "b", "ba", "bca", "bda", "bdca"]);
