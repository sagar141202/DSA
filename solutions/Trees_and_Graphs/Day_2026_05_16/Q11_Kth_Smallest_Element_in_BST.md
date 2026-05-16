# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The binary search tree is defined as a binary tree where for every node, the values in the left subtree are less than the node's value, and the values in the right subtree are greater than the node's value. The problem can be solved by performing an in-order traversal of the BST and returning the kth element. The constraints are that the number of nodes in the tree is between 1 and 10^4, and k is between 1 and the number of nodes.

## Approach
The algorithm uses in-order traversal to visit nodes in ascending order. It keeps track of the current node index and returns the node's value when the index equals k. The traversal is recursive or iterative, depending on the implementation.

## Complexity
- Time: O(N)
- Space: O(H)

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
Input: root = [3,1,4,null,2], k = 1
Output: 1
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

## Key Takeaways
- In-order traversal visits nodes in ascending order in a binary search tree.
- Iterative in-order traversal uses a stack to avoid recursion.
- The kth smallest element is found by keeping track of the current index during the traversal.