const list = [
  { name: "조준형", age: 31, height: 190 },
  { name: "조준형", age: 32, height: 190 },
  { name: "조준형", age: 33, height: 190 },
  { name: "조준형", age: 33, height: 170 },
  { name: "조준형", age: 33, height: 200 },
  { name: "가준형", age: 33, height: 200 },
  { name: "다준형", age: 33, height: 200 },
];
list.sort((a, b) => {
  if (a.age !== b.age) {
    return a.age - b.age;
  } else if (a.height !== b.height) {
    return a.height - b.height;
  } else {
    return a.name - b.name;
  }
});
console.log(list);
