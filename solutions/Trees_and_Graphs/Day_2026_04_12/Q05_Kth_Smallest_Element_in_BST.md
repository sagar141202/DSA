# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST contains unique values and is guaranteed to have at least k nodes. For example, if the BST is:
       5
      / \
     3   6
    / \
   2   4
  /
 1
The kth smallest element for k = 3 would be 3.

## Approach
We can solve this problem using an in-order traversal of the BST, which visits nodes in ascending order. We keep track of the current node index and return the node's value when the index matches k. This approach takes advantage of the BST property, where the left subtree of a node contains only nodes with values less than the node's value, and the right subtree contains only nodes with values greater than the node's value.

## Complexity
- Time: O(h + k), where h is the height of the BST
- Space: O(h), for the recursion stack in the worst case

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
        
        // Traverse the BST and find the kth smallest element
        while (curr || !s.empty()) {
            // Go as far left as possible, pushing nodes onto the stack
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // Pop the top node from the stack and decrement k
            curr = s.top();
            s.pop();
            k--;
            // If k is 0, return the current node's value
            if (k == 0) {
                return curr->val;
            }
            // Move to the right subtree
            curr = curr->right;
        }
        // If k is not found, return -1 (this should not happen)
        return -1;
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
- In-order traversal visits nodes in ascending order, making it suitable for finding the kth smallest element in a BST.
- Using a stack to store nodes for in-order traversal avoids recursion and reduces space complexity.
- This approach has a time complexity of O(h + k), where h is the height of the BST, making it efficient for large BSTs.