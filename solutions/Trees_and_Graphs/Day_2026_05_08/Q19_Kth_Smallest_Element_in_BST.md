# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have at least k nodes. The nodes of the BST are guaranteed to have unique values. For example, given the root of the following BST and k = 3, the output should be 3: 
       5
      / \
     3   6
    / \
   2   4
   /
  1

## Approach
The algorithm uses an in-order traversal of the BST to visit nodes in ascending order. It keeps track of the current node index and returns the node's value when the index reaches k. This approach takes advantage of the BST property where the left subtree of a node contains only nodes with values less than the node's value, and the right subtree contains only nodes with values greater than the node's value.

## Complexity
- Time: O(h + k), where h is the height of the tree
- Space: O(h), for the recursive call stack

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
        stack<TreeNode*> s;
        TreeNode* curr = root;
        while (curr || !s.empty()) {
            // go as far left as possible, pushing nodes onto the stack
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // pop the leftmost node from the stack and decrement k
            curr = s.top();
            s.pop();
            k--;
            // if k reaches 0, return the current node's value
            if (k == 0) return curr->val;
            // move to the right subtree
            curr = curr->right;
        }
        // if k is still greater than 0, the tree has fewer than k nodes
        return -1; // or throw an exception
    }
};
```

## Test Cases
```
Input: root = [5,3,6,2,4,1], k = 3
Output: 3
Input: root = [5,3,6,2,4,1], k = 1
Output: 1
```

## Key Takeaways
- The in-order traversal of a BST visits nodes in ascending order.
- Using a stack to implement the in-order traversal allows for an iterative solution.
- The algorithm has a time complexity of O(h + k) due to the potential need to traverse the height of the tree and visit k nodes.