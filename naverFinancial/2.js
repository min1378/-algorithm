const Element = function (value) {
  this._value = value;
};
Element.prototype.value = function () {
  return this._value;
};

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  const T = A.map((element) => new Element(element));
  return T;
}
const T = solution([1, 2, 3]);
console.log(T[0].value());
console.log(T[0]._value);
console.log(T[1].value === T[0].value);
console.log(T[0].hasOwnProperty("_value"));
console.log(T[1].value());
console.log(T[2].value());
