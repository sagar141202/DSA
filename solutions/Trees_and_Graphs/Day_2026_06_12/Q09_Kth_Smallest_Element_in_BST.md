# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have k nodes. The nodes in the BST have distinct values. For example, if the input BST is `    5
   / \
  3   6
 / \
2   4`, and k = 3, the output should be 3, because the in-order traversal of the BST is [2, 3, 4, 5, 6] and the 3rd smallest element is 3.

## Approach
The approach is to use in-order traversal of the BST, which visits nodes in ascending order. We will keep track of the current node index and return the node value when the index reaches k.

## Complexity
- Time: O(h + k), where h is the height of the tree, because we are traversing the tree using in-order traversal.
- Space: O(h), for the recursion stack in the worst case when the tree is skewed.

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
        TreeNode* current = root;
        while (current || !s.empty()) {
            // Traverse to the leftmost node
            while (current) {
                s.push(current);
                current = current->left;
            }
            // Visit the node and decrement k
            current = s.top();
            s.pop();
            k--;
            if (k == 0) {
                return current->val;
            }
            // Move to the right subtree
            current = current->right;
        }
        return -1; // Should not reach here
    }
};
```

## Test Cases
```
Input: 
    5
   / \
  3   6
 / \
2   4
k = 3
Output: 3
```

## Key Takeaways
- The problem can be solved using in-order traversal of the BST.
- We can use a stack to simulate the recursion stack for in-order traversal.
- The time complexity is O(h + k) because we are traversing the tree and keeping track of the current index.