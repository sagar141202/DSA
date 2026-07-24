# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST contains unique integers, and for each node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. The function should return the kth smallest element in the BST. If the kth smallest element does not exist, return -1. For example, given the BST with the following structure:
       5
      / \
     3   6
    / \
   2   4
  /
 1
and k = 3, the function should return 3, because the inorder traversal of the BST is [1, 2, 3, 4, 5, 6] and the 3rd smallest element is 3.

## Approach
We can solve this problem using an inorder traversal of the BST, which visits nodes in ascending order. We can use a stack to implement the inorder traversal iteratively. We keep track of the current node and the number of nodes visited.

## Complexity
- Time: O(h + k), where h is the height of the BST
- Space: O(h), where h is the height of the BST

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
            // go as far left as possible
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // visit the node
            curr = s.top();
            s.pop();
            k--;
            if (k == 0) {
                return curr->val;
            }
            // move to the right subtree
            curr = curr->right;
        }
        return -1; // if k is larger than the number of nodes
    }
};
```

## Test Cases
```
Input: root = [5,3,6,2,4,1], k = 3
Output: 3
Input: root = [5,3,6,2,4,1], k = 6
Output: 6
Input: root = [5,3,6,2,4,1], k = 7
Output: -1
```

## Key Takeaways
- Use inorder traversal to visit nodes in ascending order
- Implement inorder traversal iteratively using a stack to avoid recursion
- Keep track of the number of nodes visited to find the kth smallest element