const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
// const check = `9
// 0
// 12345678
// 32
// `;
// const input = check.split("\n");

class Heap {
  constructor(compare) {
    this.heapContainer = [];
    this.compare = compare;
  }
  size() {
    return this.heapContainer.length;
  }
  swap(a, b) {
    const temp = this.heapContainer[a];
    this.heapContainer[a] = this.heapContainer[b];
    this.heapContainer[b] = temp;
  }
  getParentIndex(childIndex) {
    return Math.floor((childIndex - 1) / 2);
  }
  getLeftChildIndex(parentIndex) {
    return parentIndex * 2 + 1;
  }
  getRightChildIndex(parentIndex) {
    return parentIndex * 2 + 2;
  }
  peak() {
    return this.heapContainer[0];
  }
  add(item) {
    let index = this.heapContainer.push(item) - 1;
    let parentIndex = this.getParentIndex(index);

    while (parentIndex >= 0 && this.compare(this.heapContainer[index], this.heapContainer[parentIndex])) {
      this.swap(index, parentIndex);
      index = parentIndex;
      parentIndex = this.getParentIndex(index);
    }
  }
  poll() {
    if (this.size() < 2) return this.heapContainer.pop();
    const item = this.peak();
    this.heapContainer[0] = this.heapContainer.pop();
    let index = 0;
    let leftIndex = this.getLeftChildIndex(index);
    let rightIndex = this.getRightChildIndex(index);
    while (leftIndex < this.size()) {
      const target = rightIndex < this.size() && this.compare(this.heapContainer[rightIndex], this.heapContainer[leftIndex]) ? rightIndex : leftIndex;
      if (this.compare(this.heapContainer[index], this.heapContainer[target])) break;
      this.swap(index, target);
      index = target;
      leftIndex = this.getLeftChildIndex(index);
      rightIndex = this.getRightChildIndex(index);
    }

    return item;
  }
}

const [N, ...list] = input;
const data = list.map(Number);
const compare = (a, b) => a < b;
const heap = new Heap(compare);
let result = "";
for (let i = 0; i < N; i++) {
  if (data[i]) {
    heap.add(data[i]);
  }
  if (!data[i]) {
    const item = heap.poll();
    result += `${item ? item : 0}\n`;
  }
}
console.log(result);
