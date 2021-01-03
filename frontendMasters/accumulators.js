function joinElements(array, joinString) {
  function recurse(index, resultSoFar) {
    resultSoFar += array[index];
    console.log(resultSoFar);
    if (index === array.length - 1) {
      console.log("hi", resultSoFar);
      return resultSoFar;
    }
    recurse(index + 1, resultSoFar);
  }
  console.log(recurse(0, joinString));
}

console.log(joinElements(["a", "p", "p", "l", "e"], ""));
