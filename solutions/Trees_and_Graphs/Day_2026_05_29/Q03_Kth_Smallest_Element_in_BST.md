# Kth Smallest Element in BST

## Problem Statement
Given a Binary Search Tree (BST) and an integer k, find the kth smallest element in the BST. The BST is defined as a binary tree where for each node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The function should return the kth smallest element if it exists, otherwise return -1. The input BST is non-empty and k is a positive integer.

## Approach
We will use an in-order traversal of the BST to get the elements in ascending order. Then we can simply return the kth element from the result. The in-order traversal visits the left subtree, the current node, and then the right subtree.

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
    int kthSmallest(TreeNode* root, int k) {
        // Initialize a stack to store nodes for in-order traversal
        stack<TreeNode*> s;
        TreeNode* curr = root;
        
        // Traverse the tree and push nodes to the stack
        while (curr || !s.empty()) {
            // Go as far left as possible and push nodes to the stack
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            
            // Pop a node from the stack and decrement k
            curr = s.top();
            s.pop();
            k--;
            
            // If k is 0, return the current node's value
            if (k == 0) return curr->val;
            
            // Move to the right subtree
            curr = curr->right;
        }
        
        // If k is not found, return -1
        return -1;
    }
};
```

## Test Cases
```
Input: 
   5
  / \
 3   6
/ \
2   4
k = 3
Output: 3

Input: 
   5
  / \
 3   6
/ \
2   4
k = 5
Output: 6
```

## Key Takeaways
- Use in-order traversal to get elements in ascending order from a BST.
- Utilize a stack to efficiently perform in-order traversal.
- Keep track of the current node and the value of k to find the kth smallest element.