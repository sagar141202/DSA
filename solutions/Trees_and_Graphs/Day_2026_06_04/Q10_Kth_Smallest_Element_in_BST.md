# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have k nodes. The nodes in the BST have unique values. For example, if the input BST is:
       5
      / \
     3   6
    / \
   2   4
  /
 1
And k = 3, the output should be 3, because the in-order traversal of the BST is [1, 2, 3, 4, 5, 6] and the 3rd smallest element is 3.

## Approach
The approach to solve this problem is to perform an in-order traversal of the BST, which visits the nodes in ascending order. We can use a recursive or iterative approach to traverse the tree and keep track of the current node index.

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
            // go as left as possible
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
            // go right
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
```

## Key Takeaways
- In-order traversal visits nodes in ascending order in a BST
- We can use a stack to perform iterative in-order traversal
- Keep track of the current node index to find the kth smallest element