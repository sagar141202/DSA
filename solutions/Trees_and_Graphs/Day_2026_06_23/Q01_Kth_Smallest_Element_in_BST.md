# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, find the kth smallest element in the BST. The BST is guaranteed to have k nodes. The problem can be solved by performing an in-order traversal of the BST and returning the kth node. For example, given the root of the BST [5,3,6,2,4,7] and k = 3, the kth smallest element is 3.

## Approach
The approach to solve this problem is to perform an in-order traversal of the BST, which visits nodes in ascending order. We can use a recursive or iterative approach to traverse the tree and keep track of the current node index.

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
            // Visit the current node
            curr = s.top();
            s.pop();
            k--;
            if (k == 0) {
                return curr->val;
            }
            // Traverse to the right subtree
            curr = curr->right;
        }
        return -1; // Should not reach here
    }
};
```

## Test Cases
```
Input: root = [5,3,6,2,4,7], k = 3
Output: 3
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

## Key Takeaways
- Use in-order traversal to visit nodes in ascending order
- Utilize a stack to perform iterative in-order traversal
- Keep track of the current node index to find the kth smallest element