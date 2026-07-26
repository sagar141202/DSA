# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have k nodes. The nodes in the BST have distinct values. For example, if the input BST is:
       5
      / \
     3   6
    / \
   2   4
  /
 1
And k = 3, the output should be 3, which is the 3rd smallest element in the BST.

## Approach
We can solve this problem using an in-order traversal of the BST, which visits nodes in ascending order. We keep track of the current node index and return the node's value when the index reaches k. This approach takes advantage of the BST property, where the left subtree of a node contains only nodes with values less than the node's value, and the right subtree contains only nodes with values greater than the node's value.

## Complexity
- Time: O(h + k), where h is the height of the BST
- Space: O(h), for the recursion stack

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
            // go as left as possible
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // backtrack
            curr = s.top();
            s.pop();
            k--;
            if (k == 0) {
                return curr->val;
            }
            curr = curr->right;
        }
        return -1; // not found
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
- Use in-order traversal to visit nodes in ascending order
- Keep track of the current node index to find the kth smallest element
- The time complexity is O(h + k) due to the traversal and the space complexity is O(h) for the recursion stack