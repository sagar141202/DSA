# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree node has a value and two children: left and right. The function should return a vector of integers representing the inorder traversal of the binary tree. For example, given the binary tree [4,2,5,1,3], the function should return [1,2,3,4,5]. The binary tree is defined as follows: the root node is 4, the left child of 4 is 2, the right child of 4 is 5, the left child of 2 is 1, and the right child of 2 is 3.

## Approach
The approach is to use a recursive or iterative method to traverse the binary tree in inorder. We start by visiting the left subtree, then the current node, and finally the right subtree. This can be achieved using a stack to store nodes to be visited.

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
        TreeNode* current = root;
        
        while (current != NULL || !s.empty()) {
            // go as far left as possible, pushing nodes onto the stack
            while (current != NULL) {
                s.push(current);
                current = current->left;
            }
            
            // backtracking, pop node from stack and visit it
            current = s.top();
            s.pop();
            result.push_back(current->val);
            
            // go right
            current = current->right;
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
- Inorder traversal visits the left subtree, the current node, and then the right subtree.
- We can use recursion or iteration with a stack to achieve inorder traversal.
- The time complexity of inorder traversal is O(n), where n is the number of nodes in the binary tree.