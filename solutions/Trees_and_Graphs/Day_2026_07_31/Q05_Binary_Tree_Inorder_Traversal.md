# Binary Tree Inorder Traversal

## Problem Statement
Given the root of a binary tree, return the inorder traversal of its nodes' values. Inorder traversal visits the left subtree, the current node, and then the right subtree. The binary tree node has a value, a left child node, and a right child node. The problem statement requires a function that takes the root of the binary tree as input and returns a vector of integers representing the inorder traversal of the binary tree. For example, given the binary tree [4,2,5,1,3], the function should return [1,2,3,4,5].

## Approach
The algorithm uses a recursive or iterative approach to traverse the binary tree in inorder. It first visits the left subtree, then the current node, and finally the right subtree. This can be achieved using a stack to store nodes to be visited.

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
        stack<TreeNode*> st;
        TreeNode* curr = root;
        
        while (curr || !st.empty()) {
            // Traverse to the leftmost node
            while (curr) {
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
Input: []
Output: []
```

## Key Takeaways
- Inorder traversal visits the left subtree, the current node, and then the right subtree.
- A stack can be used to store nodes to be visited during the traversal.
- The time complexity is O(n), where n is the number of nodes in the binary tree, because each node is visited once.