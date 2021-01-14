class Tree {
  constructor(question) {
    this.question = question;
    this.yes = null;
    this.no = null;
  }
  insertChild(question, side) {
    const newQuestion = new Tree(question);
    this[side] = newQuestion;
    return newQuestion;
  }
  removeChild(value) {}
}

const myTree = new Tree(1);
const myTree2 = myTree.insertChild(2);
console.log(myTree);
console.log(myTree2);
