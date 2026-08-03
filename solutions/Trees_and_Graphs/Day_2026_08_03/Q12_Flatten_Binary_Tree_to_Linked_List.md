# Flatten Binary Tree to Linked List

## Problem Statement
Given the root of a binary tree, flatten the tree into a linked list in-place, where the left child of each node becomes the right child and the original right child becomes the next node in the list. The binary tree is defined as follows: each node has a value, and two child nodes (left and right) which are also nodes or null. The root of the binary tree is given as the input, and the output should be the root of the flattened linked list. For example, given the binary tree:
```
    1
   / \
  2   5
 / \   \
3   4   6
```
The output should be:
```
1 -> 2 -> 3 -> 4 -> 5 -> 6
```
The constraints are that the number of nodes in the tree will not exceed 100, and the values of the nodes are in the range [0, 100].

## Approach
The approach to solve this problem is to use a recursive function to traverse the binary tree in pre-order (root, left, right), and then append the left and right subtrees to the right child of the current node. We will also keep track of the previous node to update its right child.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void flatten(TreeNode* root) {
        if (root == nullptr) return;
        flatten(root->left);
        flatten(root->right);
        if (root->left != nullptr) {
            // find the rightmost node in the left subtree
            TreeNode* rightmost = root->left;
            while (rightmost->right != nullptr) {
                rightmost = rightmost->right;
            }
            // append the right subtree to the right child of the rightmost node
            rightmost->right = root->right;
            // update the right child of the current node
            root->right = root->left;
            // remove the left child of the current node
            root->left = nullptr;
        }
    }
};
```

## Test Cases
```
Input: [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

## Key Takeaways
- Use recursion to traverse the binary tree in pre-order.
- Append the left and right subtrees to the right child of the current node.
- Keep track of the previous node to update its right child.