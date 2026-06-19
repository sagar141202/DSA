# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree node has the following structure: a node with an integer value and two child nodes (left and right). The root of the binary tree is given, and the function should return a vector of integers representing the inorder traversal of the binary tree.

## Approach
The algorithm uses a recursive or iterative approach to traverse the binary tree in an inorder manner. It starts by visiting the left subtree, then the current node, and finally the right subtree. This can be achieved using a stack to store nodes or through recursive function calls.

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
        stack<TreeNode*> st;
        TreeNode* curr = root;
        
        while (curr != nullptr || !st.empty()) {
            // Traverse to the leftmost node
            while (curr != nullptr) {
                st.push(curr);
                curr = curr->left;
            }
            
            // Visit the node and move to the right subtree
            curr = st.top();
            st.pop();
            result.push_back(curr->val);
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
```

## Key Takeaways
- Use a stack to store nodes for iterative inorder traversal.
- Recursive function calls can also be used for inorder traversal, but may lead to stack overflow errors for very large trees.
- Inorder traversal visits nodes in ascending order for a binary search tree.