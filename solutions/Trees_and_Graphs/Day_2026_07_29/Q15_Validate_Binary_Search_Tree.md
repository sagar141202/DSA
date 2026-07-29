# Validate Binary Search Tree

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The tree must also satisfy the BST property for all nodes. Constraints: The number of nodes in the tree is in the range [1, 10^4]. The input is guaranteed to be a binary tree, but it may not be a BST. Examples: Input: root = [2,1,3], Output: true; Input: root = [5,1,4,null,null,3,6], Output: false.

## Approach
The algorithm involves performing an in-order traversal of the binary tree and checking if the resulting sequence is sorted in ascending order. If the sequence is sorted, then the binary tree is a valid BST. This approach works because in a BST, an in-order traversal always yields a sorted sequence.

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
    bool isValidBST(TreeNode* root) {
        // Initialize a stack to store nodes for in-order traversal
        stack<TreeNode*> st;
        TreeNode* prev = nullptr;
        
        // Traverse the tree
        while (root || !st.empty()) {
            // Go as far left as possible
            while (root) {
                st.push(root);
                root = root->left;
            }
            
            // Backtrack and check the node's value
            root = st.top();
            st.pop();
            
            // If this is not the first node and the current node's value is not greater than the previous node's value, return false
            if (prev && root->val <= prev->val) {
                return false;
            }
            
            // Update the previous node
            prev = root;
            
            // Move to the right subtree
            root = root->right;
        }
        
        // If we've traversed the entire tree without finding any issues, return true
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
- A valid BST must satisfy the property that all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node.
- In-order traversal of a BST always yields a sorted sequence in ascending order.
- The algorithm has a time complexity of O(n) and a space complexity of O(n) due to the recursive call stack or explicit stack used for traversal.