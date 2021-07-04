class Heap {
  constructor(comp) {
    this.comp = comp;
    this.heapContainer = [];
  }
  getLeftChildIndex(index) {
    return 2 * index + 1;
  }
  getRightChildIndex(index) {
    return 2 * index + 2;
  }
  getParentIndex(index) {
    return Math.floor((index - 1) / 2);
  }
  hasParent(index) {
    return this.getParentIndex(index) >= 0;
  }
  hasLeftChild(index) {
    return this.getLeftChildIndex(index) < this.heapContainer.length;
  }
  hasRightChild(index) {
    return this.getRightChildIndex(index) < this.heapContainer.length;
  }
  leftChild(index) {
    return this.heapContainer[this.getLeftChildIndex(index)];
  }
  rightChild(index) {
    return this.heapContainer[this.getRightChildIndex(index)];
  }
  parent(index) {
    return this.heapContainer[this.parent(index)];
  }
  swap(a, b) {
    const temp = this.heapContainer[a];
    this.heapContainer[a] = this.heapContainer[b];
    this.heapContainer[b] = temp;
  }
  peek() {
    if (this.heapContainer.length === 0) {
      return null;
    }
    return this.heapContainer[0];
  }
  isEmpty() {
    return !this.heapContainer.length;
  }
  toString() {
    return this.heapContainer.toString();
  }
  heapifyUp(index) {
    let currentIndex = index || this.heapContainer.length - 1;
    while (this.hasParent(currentIndex) && !this.comp(this.parent(currentIndex), this.heapContainer[currentIndex])) {
      this.swap(currentIndex, this.getParentIndex(currentIndex));
      currentIndex = this.getParentIndex(currentIndex);
    }
  }
  heapifyDown(index = 0) {
    let currentIndex = index;
    let nextIndex = null;
    while (this.hasLeftChild(currentIndex)) {
      if (this.hasRightChild(currentIndex) && this.comp(this.rightChild(currentIndex), this.leftChild(currentIndex))) {
        nextIndex = this.getRightChildIndex(currentIndex);
      } else {
        nextIndex = this.getLeftChildIndex(currentIndex);
      }
      if (this.comp(this.heapContainer[currentIndex], this.heapContainer[nextIndex])) {
        break;
      }
      this.swap(currentIndex, nextIndex);
      currentIndex = nextIndex;
    }
  }
  find(item) {
    const foundItemIndices = [];
    for (let itemIndex = 0; itemIndex < this.heapContainer.length; itemIndex += 1) {
      if (item === this.heapContainer[itemIndex]) {
        foundItemIndices.push(itemIndex);
      }
    }
    return foundItemIndices;
  }
  poll() {
    if (this.heapContainer.length === 0) {
      return null;
    }
    if (this.heapContainer.length === 1) {
      return this.heapContainer.pop();
    }
    const item = this.heapContainer[0];
    this.heapContainer[0] = this.heapContainer.pop();
    this.heapifyDown();
    return item;
  }
  add(item) {
    this.heapContainer.push(item);
    this.heapifyUp();
    return this;
  }
  remove(item) {
    const numberOfItemsToRemove = this.find(item).length;
    for (let iteration = 0; iteration < numberOfItemsToRemove; iteration += 1) {
      const indexToRemove = this.find(item).pop();
      if (indexToRemove === this.heapContainer.length - 1) {
        this.heapContainer.pop();
      } else {
        this.heapContainer[indexToRemove] = this.heapContainer.pop();
      }
      const parentItem = this.parent(indexToRemove);
      if (this.hasLeftChild(indexToRemove) && (!parentItem || this.comp(parentItem, this.heapContainer[indexToRemove]))) {
        this.heapifyDown(indexToRemove);
      } else {
        this.heapifyUp(indexToRemove);
      }
    }
    return this;
  }
}
