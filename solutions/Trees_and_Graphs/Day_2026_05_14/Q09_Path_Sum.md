# Path Sum

## Problem Statement
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children. The path must start at the root and end at a leaf node. For example, given the binary tree with root [5,4,8,11,null,13,4,7,2,null,null,5,1] and target sum 22, the function should return true because the path 5 -> 4 -> 11 -> 2 sums to 22.

## Approach
The solution involves recursively traversing the binary tree, keeping track of the current sum of node values from the root to the current node. If the current node is a leaf node and the current sum equals the target sum, return true.

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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        // Base case: if the tree is empty, return false
        if (!root) return false;
        
        // Recursive case: if the current node is a leaf node and the current sum equals the target sum, return true
        if (!root->left && !root->right) return root->val == targetSum;
        
        // Recursively traverse the left and right subtrees
        return hasPathSum(root->left, targetSum - root->val) || hasPathSum(root->right, targetSum - root->val);
    }
};
```

## Test Cases
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: true
Input: root = [1,2,3], targetSum = 5
Output: false
```

## Key Takeaways
- The problem can be solved using recursive depth-first search (DFS) traversal of the binary tree.
- It's essential to handle the base case where the tree is empty and the recursive case where the current node is a leaf node.
- The time complexity is O(N), where N is the number of nodes in the tree, because each node is visited once.