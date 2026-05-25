# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, return the kth smallest element in the BST. The problem assumes that the BST contains unique values and that k is within the range of the number of nodes in the BST. For example, if we have a BST with the following structure: 
       5
      / \
     3   6
    / \
   2   4
  /
 1
And k = 3, the function should return 3, because 3 is the 3rd smallest element in the BST.

## Approach
The algorithm uses an in-order traversal of the BST to visit nodes in ascending order. It keeps track of the current node index and returns the node's value when the index matches k.

## Complexity
- Time: O(n)
- Space: O(h)

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
        TreeNode* curr = root;
        
        // Traverse the tree and keep track of the current node index
        while (curr || !s.empty()) {
            // Go as far left as possible
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // Visit the current node
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
        // If k is not found, return -1
        return -1;
    }
};
```

## Test Cases
```
Input: root = [5,3,6,2,4,1], k = 3
Output: 3
```

## Key Takeaways
- Use in-order traversal to visit nodes in ascending order.
- Keep track of the current node index to find the kth smallest element.
- Use a stack to store nodes for efficient traversal.