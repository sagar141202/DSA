# Kth Smallest Element in BST

## Problem Statement
Given the root of a binary search tree (BST) and an integer k, return the kth smallest element in the BST. The solution should handle cases where k is within the range of the number of nodes in the tree. If k is larger than the number of nodes, the function should return -1. For example, given the BST with nodes [5, 3, 6, 2, 4, 7] and k = 3, the function should return 3, which is the 3rd smallest element in the BST.

## Approach
The approach involves using an in-order traversal of the BST to visit nodes in ascending order, then selecting the kth element from the traversal. This method works because BSTs are ordered such that the left subtree of a node contains only nodes with keys less than the node's key, and the right subtree contains only nodes with keys greater than the node's key.

## Complexity
- Time: O(n)
- Space: O(n)

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
        int count = 0;
        
        while (curr || !s.empty()) {
            // Traverse to the leftmost node
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            
            // Backtrack and visit the node
            curr = s.top();
            s.pop();
            count++;
            
            // If this is the kth node, return its value
            if (count == k) {
                return curr->val;
            }
            
            // Move to the right subtree
            curr = curr->right;
        }
        
        // If k is larger than the number of nodes, return -1
        return -1;
    }
};
```

## Test Cases
```
Input: root = [5, 3, 6, 2, 4, 7], k = 3
Output: 3
Input: root = [5, 3, 6, 2, 4, 7], k = 10
Output: -1
```

## Key Takeaways
- In-order traversal of a BST visits nodes in ascending order.
- Using a stack to perform in-order traversal allows for efficient traversal without recursion.
- The kth smallest element can be found by counting the number of nodes visited during the traversal.