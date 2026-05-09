# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, then the current node, and finally the right subtree. The function should take the root of the binary tree as input and return a vector of integers representing the inorder traversal of the tree. For example, given the binary tree `[4,2,5,1,3]`, the function should return `[1,2,3,4,5]`. The binary tree node structure is defined as `TreeNode* root`, where each node has an integer value and pointers to its left and right children.

## Approach
The algorithm uses a recursive or iterative approach to traverse the binary tree in inorder. It visits the left subtree, then the current node, and finally the right subtree. This can be achieved using a stack to store nodes to be visited or by recursive function calls.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> s;
        TreeNode* curr = root;
        
        while (curr != NULL || !s.empty()) {
            // Traverse to the leftmost node
            while (curr != NULL) {
                s.push(curr);
                curr = curr->left;
            }
            
            // Backtrack and visit the node
            curr = s.top();
            s.pop();
            result.push_back(curr->val);
            
            // Move to the right subtree
            curr = curr->right;
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: [4,2,5,1,3]
Output: [1,2,3,4,5]
Input: [1]
Output: [1]
Input: []
Output: []
```

## Key Takeaways
- Inorder traversal visits nodes in ascending order for a binary search tree.
- Recursive and iterative approaches can be used to solve the problem, with the iterative approach using a stack to store nodes to be visited.
- The time complexity is O(n), where n is the number of nodes in the tree, since each node is visited once.