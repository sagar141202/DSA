# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree node has the following structure: a node with an integer value and two child nodes (left and right). The input tree is guaranteed to be non-empty, and each node has a unique integer value. For example, given the following binary tree: 
       4
     /   \
    2     6
   / \   / \
  1   3 5   7
The inorder traversal of this tree is [1, 2, 3, 4, 5, 6, 7].

## Approach
We will use recursion to traverse the left subtree, visit the current node, and then traverse the right subtree. This approach ensures that we visit the nodes in the correct order. We can also use iteration with a stack to achieve the same result.

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
        traverse(root, result);
        return result;
    }
    
    void traverse(TreeNode* node, vector<int>& result) {
        if (node == nullptr) return;
        traverse(node->left, result);
        result.push_back(node->val);
        traverse(node->right, result);
    }
};
```

## Test Cases
```
Input: [4,2,6,1,3,5,7]
Output: [1,2,3,4,5,6,7]
Input: [1]
Output: [1]
```

## Key Takeaways
- Inorder traversal visits the left subtree, the current node, and then the right subtree.
- Recursion is a natural fit for tree traversal problems.
- Iteration with a stack can also be used to solve tree traversal problems.