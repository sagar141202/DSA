# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. You may assume that the BST contains at least k nodes. The BST is defined as a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node. For example, given the BST with the following structure:
       5
      / \
     3   6
    / \
   2   4
  / \
 1   0
And k = 3, the kth smallest element is 3.

## Approach
The algorithm uses an in-order traversal of the BST to visit nodes in ascending order. It keeps track of the number of nodes visited and returns the kth node. This approach ensures that the kth smallest element is found efficiently.

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
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        // Initialize a stack to store nodes
        stack<TreeNode*> s;
        // Initialize a pointer to the current node
        TreeNode* curr = root;
        
        // Traverse the tree until the kth smallest element is found
        while (curr || !s.empty()) {
            // Traverse to the leftmost node
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // Visit the leftmost node
            curr = s.top();
            s.pop();
            k--;
            // If the kth smallest element is found, return its value
            if (k == 0) {
                return curr->val;
            }
            // Move to the right subtree
            curr = curr->right;
        }
        // If the kth smallest element is not found, return -1
        return -1;
    }
};
```

## Test Cases
```
Input: root = [5,3,6,2,4,1,0], k = 3
Output: 3
```

## Key Takeaways
- In-order traversal visits nodes in ascending order in a BST.
- Using a stack to store nodes allows for efficient traversal and retrieval of the kth smallest element.
- The time complexity is O(h + k) due to the traversal of the tree and the stack operations.