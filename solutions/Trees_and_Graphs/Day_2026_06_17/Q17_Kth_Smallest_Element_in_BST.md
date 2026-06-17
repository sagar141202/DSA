# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have k nodes. The problem can be solved by performing an in-order traversal of the BST and returning the kth element. The constraints are: 1 <= k <= number of nodes in the BST, and the BST has at least k nodes.

## Approach
The algorithm uses a stack-based in-order traversal to visit nodes in ascending order. It keeps track of the current node and the number of nodes visited. When the kth node is visited, its value is returned as the result.

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
            // Traverse to the leftmost node
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            // Visit the node
            curr = s.top();
            s.pop();
            k--;
            if (k == 0) {
                return curr->val;
            }
            // Traverse to the right subtree
            curr = curr->right;
        }
        return -1; // Not found
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
- In-order traversal visits nodes in ascending order for a BST.
- Using a stack to perform in-order traversal allows for efficient traversal and node visiting.
- Keeping track of the number of nodes visited helps to identify the kth smallest element.