# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree node has a value, a left child node, and a right child node. The number of nodes in the tree is in the range [0, 100]. The input tree is guaranteed to be a binary tree. For example, given the following binary tree: 
       4
     /   \
    2     6
   / \   / \
  1   3 5   7
The inorder traversal is [1, 2, 3, 4, 5, 6, 7].

## Approach
We can use recursion or iteration to perform the inorder traversal. The recursive approach involves visiting the left subtree, the current node, and then the right subtree. The iterative approach uses a stack to store nodes and visit them in the correct order. We will implement both recursive and iterative solutions.

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
        inorderTraversalHelper(root, result);
        return result;
    }

    void inorderTraversalHelper(TreeNode* node, vector<int>& result) {
        if (node == nullptr) {
            return;
        }
        inorderTraversalHelper(node->left, result);
        result.push_back(node->val);
        inorderTraversalHelper(node->right, result);
    }

    // Iterative solution
    vector<int> inorderTraversalIterative(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> nodeStack;
        TreeNode* currentNode = root;
        while (currentNode != nullptr || !nodeStack.empty()) {
            while (currentNode != nullptr) {
                nodeStack.push(currentNode);
                currentNode = currentNode->left;
            }
            currentNode = nodeStack.top();
            nodeStack.pop();
            result.push_back(currentNode->val);
            currentNode = currentNode->right;
        }
        return result;
    }
};
```

## Test Cases
```
Input: [4,2,6,1,3,5,7]
Output: [1,2,3,4,5,6,7]
Input: []
Output: []
Input: [1]
Output: [1]
```

## Key Takeaways
- Inorder traversal visits the left subtree, the current node, and then the right subtree.
- Recursion and iteration can be used to solve the problem, with recursion being more intuitive and iteration being more efficient in terms of space complexity.
- The time complexity of both solutions is O(n), where n is the number of nodes in the tree.