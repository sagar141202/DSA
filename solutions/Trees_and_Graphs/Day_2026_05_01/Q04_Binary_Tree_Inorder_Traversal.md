# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree node has a value and two children (left and right). The input tree is not guaranteed to be balanced, and it may contain duplicate values. For example, given the binary tree `[4,2,5,1,3]`, the inorder traversal is `[1,2,3,4,5]`.

## Approach
The algorithm uses a recursive or iterative approach to traverse the binary tree in an inorder manner. It first visits the left subtree, then the current node, and finally the right subtree. This can be achieved using a stack data structure to store nodes to be visited.

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
            // traverse to the leftmost node
            while (curr != nullptr) {
                st.push(curr);
                curr = curr->left;
            }
            
            // visit the node and move to the right subtree
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
Input: []
Output: []
```

## Key Takeaways
- Inorder traversal visits nodes in ascending order for a binary search tree.
- Recursive and iterative approaches can be used to solve this problem.
- The time complexity is O(n), where n is the number of nodes in the tree, because each node is visited once.