# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have at least k nodes. The nodes of the BST are guaranteed to have unique values. For example, given the BST root = [5,3,6,2,4,null,null,1], k = 3, the output should be 3 because the inorder traversal of the BST is [1,2,3,4,5,6] and the 3rd smallest element is 3.

## Approach
The approach is to use an inorder traversal of the BST, which visits nodes in ascending order, and keep track of the current node index. We can use a recursive or iterative method to perform the inorder traversal. Once we reach the kth node, we return its value as the kth smallest element.

## Complexity
- Time: O(h + k)
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
        stack<TreeNode*> s;
        TreeNode* curr = root;
        while (curr || !s.empty()) {
            // go as left as possible
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // backtracking
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
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
Input: root = [5,3,6,2,4,null,null,1], k = 1
Output: 1
```

## Key Takeaways
- Inorder traversal visits nodes in ascending order in a BST.
- Use a stack to perform iterative inorder traversal.
- Keep track of the current node index to find the kth smallest element.