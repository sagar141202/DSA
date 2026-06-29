# Kth Smallest Element in BST

## Problem Statement
Given a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is defined as a binary tree where for each node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The function should return the kth smallest element if it exists, otherwise return -1. For example, given the BST `[5,3,6,2,4,7]` and k = 3, the function should return `3` because the inorder traversal of the BST is `[2,3,4,5,6,7]` and the 3rd smallest element is `3`. If k is larger than the number of nodes in the BST, the function should return -1.

## Approach
We can solve this problem by performing an inorder traversal of the BST, which visits nodes in ascending order. We can then keep track of the current node index and return the node's value when the index matches k. The algorithm uses a stack to implement the inorder traversal iteratively.

## Complexity
- Time: O(h + k) where h is the height of the BST
- Space: O(h) for the recursion stack or the explicit stack used in the iterative solution

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
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> s;
        TreeNode* curr = root;
        while (curr || !s.empty()) {
            // go as far left as possible
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // visit the node at the top of the stack
            curr = s.top();
            s.pop();
            k--;
            if (k == 0) {
                return curr->val;
            }
            // move to the right subtree
            curr = curr->right;
        }
        // if k is larger than the number of nodes, return -1
        return -1;
    }
};
```

## Test Cases
```
Input: root = [5,3,6,2,4,7], k = 3
Output: 3
Input: root = [5,3,6,2,4,7], k = 10
Output: -1
```

## Key Takeaways
- The inorder traversal of a BST visits nodes in ascending order.
- We can use a stack to implement the inorder traversal iteratively.
- The time complexity depends on the height of the BST and the value of k.