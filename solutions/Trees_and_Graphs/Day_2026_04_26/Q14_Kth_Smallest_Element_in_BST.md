# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The solution should be efficient and scalable. For example, if the BST is:
       5
      / \
     3   6
    / \
   2   4
  /
 1
And k = 3, the output should be 3, which is the 3rd smallest element in the BST.

## Approach
We can solve this problem by using an in-order traversal of the BST, which visits nodes in ascending order. We can then keep track of the current node index and return the node value when the index equals k. This approach ensures that we find the kth smallest element efficiently.

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
        
        // Traverse the BST and keep track of the current node index
        while (curr || !s.empty()) {
            // Go as left as possible, pushing nodes onto the stack
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // Backtrack and visit the node at the top of the stack
            curr = s.top();
            s.pop();
            k--;
            // If k equals 0, return the current node value
            if (k == 0) {
                return curr->val;
            }
            // Move to the right subtree
            curr = curr->right;
        }
        // If k is not found, return -1 (not possible in this problem)
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
- Using a stack to store nodes for in-order traversal allows for an iterative solution with a time complexity of O(h + k).
- The space complexity is O(h) due to the recursion stack in the worst case, where h is the height of the BST.