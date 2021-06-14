var buildTree = function (inorder, postorder) {
  const map = {};
  inorder.forEach((value, idx) => (map[value] = idx));
  console.log(map);
  let postOrderIdx = postorder.length - 1;

  function binaryTree(start, end) {
    console.log(start, end, postOrderIdx);
    if (start > end) {
      return null;
    }

    const value = postorder[postOrderIdx--],
      idx = map[value];
    console.log("value: ", value, "index: ", idx);
    const node = new TreeNode(value);
    node.right = binaryTree(idx + 1, end);
    node.left = binaryTree(start, idx - 1);
    return node;
  }

  return binaryTree(0, inorder.length - 1);
};
function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}
console.log(buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]));
