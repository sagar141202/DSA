# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the property that for any node, all elements in the left subtree and right subtree must also follow the same property.

## Approach
The approach to solve this problem is to perform an in-order traversal of the binary tree and check if the resulting sequence is sorted in ascending order. If the sequence is sorted, then the binary tree is a valid BST. This is because in-order traversal of a BST visits nodes in ascending order.

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
    bool isValidBST(TreeNode* root) {
        // Initialize a stack to store nodes for in-order traversal
        stack<TreeNode*> st;
        TreeNode* prev = NULL;
        TreeNode* curr = root;
        
        // Perform in-order traversal
        while (curr || !st.empty()) {
            // Traverse to the leftmost node
            while (curr) {
                st.push(curr);
                curr = curr->left;
            }
            
            // Visit the node
            curr = st.top();
            st.pop();
            
            // Check if the current node's value is greater than the previous node's value
            if (prev && curr->val <= prev->val) {
                return false;
            }
            prev = curr;
            
            // Move to the right subtree
            curr = curr->right;
        }
        
        return true;
    }
};
```

## Test Cases
```
Input: root = [2,1,3]
Output: true
Input: root = [5,1,4,null,null,3,6]
Output: false
```

## Key Takeaways
- In-order traversal of a BST visits nodes in ascending order.
- We can use a stack to perform in-order traversal of a binary tree.
- Checking if the resulting sequence from in-order traversal is sorted is an efficient way to validate a BST.