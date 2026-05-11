# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST contains unique integers, and there are no duplicate values. The problem requires finding the kth smallest element in the BST, where k is a positive integer. For example, if the BST is     5
   / \
  3   6
 / \
2   4
and k = 3, the output should be 3.

## Approach
The algorithm uses an in-order traversal of the BST to visit nodes in ascending order. It utilizes a stack to efficiently traverse the tree and keeps track of the number of visited nodes to find the kth smallest element.

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
        stack<TreeNode*> s;
        TreeNode* curr = root;
        while (curr || !s.empty()) {
            // Traverse to the leftmost node
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // Visit the node and decrement k
            curr = s.top();
            s.pop();
            k--;
            if (k == 0) {
                return curr->val;
            }
            // Move to the right subtree
            curr = curr->right;
        }
        return -1; // Not found
    }
};
```

## Test Cases
```
Input: root = [5,3,6,2,4], k = 3
Output: 3
Input: root = [5,3,6,2,4], k = 1
Output: 2
```

## Key Takeaways
- In-order traversal visits nodes in ascending order in a BST.
- Using a stack allows for efficient traversal without recursion.
- Keeping track of the number of visited nodes helps find the kth smallest element.