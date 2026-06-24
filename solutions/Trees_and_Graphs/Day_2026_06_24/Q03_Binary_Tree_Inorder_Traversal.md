# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The function should take the root of the binary tree as input and return a vector of integers representing the inorder traversal of the tree. For example, given the binary tree `[4,2,5,1,3]`, the function should return `[1,2,3,4,5]`. The binary tree is defined by a `TreeNode` struct with an integer value and pointers to its left and right children.

## Approach
The algorithm uses a recursive approach to traverse the left subtree, visit the current node, and then traverse the right subtree. This is achieved through a helper function that takes the current node as input and appends its value to the result vector after traversing the left subtree. The function also handles the case where the input tree is empty.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        helper(root, result);
        return result;
    }
    
    void helper(TreeNode* node, vector<int>& result) {
        if (node == NULL) return;
        helper(node->left, result);
        result.push_back(node->val);
        helper(node->right, result);
    }
};
```

## Test Cases
```
Input: [4,2,5,1,3]
Output: [1,2,3,4,5]
Input: []
Output: []
Input: [1]
Output: [1]
```

## Key Takeaways
- Inorder traversal visits the left subtree, the current node, and then the right subtree.
- The recursive approach is suitable for tree traversals due to the recursive structure of trees.
- The time complexity is O(n) because each node is visited once, where n is the number of nodes in the tree.