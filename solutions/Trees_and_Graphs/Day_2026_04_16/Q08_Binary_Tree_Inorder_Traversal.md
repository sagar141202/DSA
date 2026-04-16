# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree has at most 100 nodes, and the values of the nodes are in the range [1, 100]. The input tree is not guaranteed to be balanced, and the height of the tree can be up to 100.

## Approach
The algorithm uses a recursive approach to traverse the binary tree in an inorder manner. It first visits the left subtree, then the current node, and finally the right subtree. This can also be achieved using iterative methods with the help of a stack data structure.

## Complexity
- Time: O(n)
- Space: O(n)

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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        inorder(root, result);
        return result;
    }
    
    void inorder(TreeNode* node, vector<int>& result) {
        if (node == nullptr) return;
        inorder(node->left, result);
        result.push_back(node->val);
        inorder(node->right, result);
    }
};
```

## Test Cases
```
Input: [1, null, 2, 3]
Output: [1, 3, 2]
Input: []
Output: []
Input: [1]
Output: [1]
```

## Key Takeaways
- Inorder traversal is a fundamental concept in tree data structures.
- Recursive and iterative methods can be used to achieve inorder traversal.
- The time complexity of inorder traversal is O(n), where n is the number of nodes in the tree, and the space complexity can be O(n) in the worst case due to the recursive call stack or the explicit stack used in the iterative method.