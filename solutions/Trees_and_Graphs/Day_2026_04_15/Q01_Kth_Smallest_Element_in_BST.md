# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have at least k nodes. The nodes of the BST are guaranteed to have distinct values. For example, given the root of the BST [5,3,6,2,4,7] and k = 3, the output should be 3, because the inorder traversal of the BST is [2,3,4,5,6,7] and the 3rd smallest element is 3.

## Approach
The approach to solve this problem is to use an inorder traversal of the BST, which visits the nodes in ascending order, and stop when we have visited k nodes. We can use a recursive or iterative approach to perform the inorder traversal.

## Complexity
- Time: O(h + k), where h is the height of the tree
- Space: O(h), where h is the height of the tree

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
    int kthSmallest(TreeNode* root, int k) {
        // Initialize a stack to store nodes
        stack<TreeNode*> st;
        // Initialize a pointer to the current node
        TreeNode* curr = root;
        // Initialize a counter to keep track of the number of nodes visited
        int count = 0;
        // Perform inorder traversal
        while (curr || !st.empty()) {
            // Go as far left as possible
            while (curr) {
                st.push(curr);
                curr = curr->left;
            }
            // Visit the current node
            curr = st.top();
            st.pop();
            count++;
            // If we have visited k nodes, return the current node's value
            if (count == k) {
                return curr->val;
            }
            // Move to the right subtree
            curr = curr->right;
        }
        // If we have not found the kth smallest element, return -1
        return -1;
    }
};
```

## Test Cases
```
Input: root = [5,3,6,2,4,7], k = 3
Output: 3
Input: root = [5,3,6,2,4,7], k = 1
Output: 2
```

## Key Takeaways
- Inorder traversal of a BST visits nodes in ascending order
- We can use a stack to perform inorder traversal iteratively
- We can stop the traversal when we have visited k nodes to find the kth smallest element in the BST