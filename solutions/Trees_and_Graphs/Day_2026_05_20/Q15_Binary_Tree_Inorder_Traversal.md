# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, then the current node, and finally the right subtree. The binary tree node has a value and two children: left and right. The inorder traversal of the following tree: 
       4
     /   \
    2     5
   / \
  1   3
is [1,2,3,4,5]. 

## Approach
The algorithm uses a recursive or iterative approach to traverse the binary tree, visiting the left subtree, the current node, and then the right subtree. This can be achieved using a stack to store nodes to be visited.

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
        
        while (curr || !st.empty()) {
            // Traverse to the leftmost node
            while (curr) {
                st.push(curr);
                curr = curr->left;
            }
            
            // Backtrack and visit the node
            curr = st.top();
            st.pop();
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
- Use a stack to store nodes to be visited for iterative traversal.
- Recursion can also be used, but it may cause a stack overflow for very large trees.
- Inorder traversal is useful for binary search trees, where it returns the nodes' values in sorted order.