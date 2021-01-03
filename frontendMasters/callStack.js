let tracker = 0;

const callMe = function () {
  tracker += 1;
  if (tracker === 3) {
    return "loops";
  }
  callMe("anyTime"); // return undefined
};

console.log(callMe());
